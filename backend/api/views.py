from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ChatMessageSerializer
from .models import ChatMessage
from ml.unified_model import UnifiedModelService
from asgiref.sync import sync_to_async, async_to_sync
import logging

logger = logging.getLogger(__name__)

class ChatbotView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            message = request.data.get('message')
            task_type = request.data.get('task_type')
            
            if not message:
                return Response(
                    {'error': 'Message is required'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Create chat message
            chat_message = ChatMessage.objects.create(
                message=message,
                response="Processing...",  # Initial response
                task_type=task_type or 'conversation'
            )
            
            # Return response
            serializer = ChatMessageSerializer(chat_message)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            logger.error(f"Error in ChatbotView: {str(e)}")
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    # Add sync version for non-async requests
    def post_sync(self, request, *args, **kwargs):
        return async_to_sync(self.post)(request, *args, **kwargs)

class ChatHistoryView(APIView):
    async def get(self, request):
        try:
            page = int(request.query_params.get('page', 1))
            page_size = int(request.query_params.get('page_size', 10))
            
            # Use sync_to_async for database operations
            messages = await sync_to_async(list)(
                ChatMessage.objects.all()[(page-1)*page_size:page*page_size]
            )
            total_count = await sync_to_async(ChatMessage.objects.count)()
            
            serializer = ChatMessageSerializer(messages, many=True)
            
            return Response({
                'results': serializer.data,
                'page': page,
                'page_size': page_size,
                'total': total_count
            })
            
        except Exception as e:
            logger.error(f"Error fetching chat history: {str(e)}")
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )