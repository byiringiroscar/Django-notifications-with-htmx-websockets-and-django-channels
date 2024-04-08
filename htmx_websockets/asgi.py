import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import core.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "htmx_websockets.settings")

application = get_asgi_application()


application = ProtocolTypeRouter({
    "http": application,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(URLRouter(core.routing.websocket_urlpatterns))
    ),
})