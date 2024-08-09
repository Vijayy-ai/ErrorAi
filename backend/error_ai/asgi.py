# """
# ASGI config for error_ai project.

# It exposes the ASGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
# """


#backend/error_ai/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from api.consumers import ChatConsumer
from chat.views import ChatbotView
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'error_ai.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            # path('wsy', ChatbotView.as_view(), name='chatbot'),
            path('ws/chat/', ChatConsumer.as_asgi()),
        ])
    ),
})



# #backend/error_ai/asgi.py
# import os
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# import api.routing


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'error_ai.settings')

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             api.routing.websocket_urlpatterns
#         )
#     ),
# })
