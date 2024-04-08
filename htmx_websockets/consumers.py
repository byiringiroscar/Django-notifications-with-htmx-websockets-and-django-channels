import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
    
    def disconnect(self, close_code):
        pass