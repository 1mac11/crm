from asgiref.sync import async_to_sync
from asyncio.log import logger
from django.db.models.signals import post_save
from django.dispatch import receiver
from .alerter import Alerter

from .models import Product
from channels.layers import get_channel_layer


@receiver(post_save, sender=Product)
def send_message(sender, instance, created, **kwargs):
    try:
        action = 'created' if created else 'updated'
        text = f'{instance} {action}'

        async_to_sync(get_channel_layer().group_send)(
            f"{instance.company.owner.id}-notifications", {"type": "send_last_message", "text": text}
        )

        tg_alert = Alerter.from_environment()
        tg_alert.custom_send_message(text)

    except Exception as e:
        logger.error(e)
