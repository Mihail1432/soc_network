import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'soc_network.settings')

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            __import__('chat.routing', fromlist=['websocket_urlpatterns']).websocket_urlpatterns
        )
    ),
})