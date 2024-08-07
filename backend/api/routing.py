
# # backend/api/routing.py
# from chat.routing import websocket_urlpatterns as chat_websocket_urlpatterns
# from django.urls import re_path
# from . import consumers

# websocket_urlpatterns = [
#     re_path(r'ws/chat/$', consumers.ChatConsumer.as_asgi()),
#     *chat_websocket_urlpatterns,
# ]


# backend/api/routing.py
from django.urls import re_path
from api.cunsumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/$', ChatConsumer.as_asgi()),
]

