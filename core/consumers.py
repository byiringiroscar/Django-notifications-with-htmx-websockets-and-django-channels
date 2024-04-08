import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.template.loader import get_template


class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope["user"] # get the user from the scope object of the connection instance
        # send a message to the client that has connected, with no content at this time
        if not self.user.is_authenticated: # if the user is not authenticated, close the connection
            self.close()
            return
        self.GROUP_NAME = "user-notifications"
        async_to_sync(self.channel_layer.group_add)(self.GROUP_NAME, self.channel_name)
        self.accept()
    
    def disconnect(self, close_code):
        if self.user.is_authenticated:
            async_to_sync(self.channel_layer.group_discard)(self.GROUP_NAME, self.channel_name)

    

    def user_joined(self, event):
        html = get_template("core/partials/notification.html").render(
            context={"username": event["text"]}
        )

        self.send(text_data=html)