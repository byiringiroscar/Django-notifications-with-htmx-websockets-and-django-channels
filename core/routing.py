from django.urls import re_path, path
from core.consumers import NotificationConsumer

ws_patterns = [
    path('ws/notifications/', NotificationConsumer.as_asgi())
]