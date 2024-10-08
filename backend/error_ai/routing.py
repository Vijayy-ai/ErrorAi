# # backend/error_ai/routing.py
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from django.urls import path
# from chat.consumers import ChatConsumer
# import api.routing

# application = ProtocolTypeRouter({
#     'websocket': AuthMiddlewareStack(
#         URLRouter([
#             path('ws/chat/', ChatConsumer.as_asgi()),
#             # Include the API routing
#             *api.routing.websocket_urlpatterns
#         ])
#     ),
# })




# backend/error_ai/routing.py
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import api.routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(api.routing.websocket_urlpatterns)
    ),
})