# #backend/chat/consumers.py
# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from api.models import ChatHistory
# from services.unified_model import unified_model

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#     async def disconnect(self, close_code):
#         pass

#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         response = await unified_model.process_input(message)
        
#         await self.create_chat_history(message, response)

#         await self.send(text_data=json.dumps({
#             'message': response
#         }))

#     async def create_chat_history(self, message, response):
#         await ChatHistory.objects.create(
#             user=self.scope["user"],
#             message=message,
#             response=response
#         )