from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def send_notification_on_signup(sender, instance, created, **kwargs):
    if created:
        # trigger notification to all consumers in the 'user-notification' group
        channel_layer = get_channel_layer()
        group_name = 'user-notifications'
        event  = {
            'type': 'user_joined',
            'username': instance.username,
        }