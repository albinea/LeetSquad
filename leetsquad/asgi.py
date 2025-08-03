import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack  # 👈 required
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'leetsquad.settings')
django.setup()

import core.routing

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(  # 👈 wrap WebSocket routes here
        URLRouter(
            core.routing.websocket_urlpatterns
        )
    ),
})
