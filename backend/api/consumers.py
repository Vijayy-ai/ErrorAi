# backend/api/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from ml.unified_model import UnifiedModelService
from .models import ChatMessage
from asgiref.sync import sync_to_async
import logging

logger = logging.getLogger(__name__)

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.model_service = UnifiedModelService()
        await self.accept()
        logger.info("WebSocket connected successfully")

    async def disconnect(self, close_code):
        logger.info(f"WebSocket disconnected with code: {close_code}")

    @sync_to_async
    def save_chat_message(self, message: str, response: str, task_type: str):
        ChatMessage.objects.create(
            message=message,
            response=response,
            task_type=task_type
        )

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            message = data.get('message')
            task_type = data.get('task_type')

            if not message:
                await self.send(text_data=json.dumps({
                    'error': 'Message is required'
                }))
                return

            # Process message
            result = await self.model_service.process_input(message, task_type)
            
            if result.get('success', False):
                # Save to database
                await self.save_chat_message(
                    message=message,
                    response=result['response'],
                    task_type=result['task_type']
                )
                
                # Send success response
                await self.send(text_data=json.dumps({
                    'user_message': message,
                    'bot_response': result['response'],
                    'task_type': result['task_type']
                }))
            else:
                # Send error response
                await self.send(text_data=json.dumps({
                    'error': result.get('error', 'Unknown error occurred')
                }))
            
        except Exception as e:
            logger.error(f"Error in WebSocket receive: {str(e)}")
            await self.send(text_data=json.dumps({
                'error': str(e)
            }))
