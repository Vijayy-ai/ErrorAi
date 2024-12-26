# """
# ASGI config for error_ai project.

# It exposes the ASGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
# """


#backend/error_ai/asgi.py
import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.apps import apps

# Set up Django ASGI application early to ensure apps are loaded
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'error_ai.settings')
django.setup()  # This is the key addition

# Import after django setup
from api.routing import websocket_urlpatterns
from api.middleware import WebSocketRateLimitMiddleware

# Initialize Django ASGI application early
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(websocket_urlpatterns)
        )
    ),
})
