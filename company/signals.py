from asgiref.sync import async_to_sync, sync_to_async
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Product
from channels.layers import get_channel_layer


# @receiver(pre_save, sender=Product)
# def send_message(sender, instance, **kwargs):
#     print(Product.objects.get(pk=instance.pk))

@receiver(post_save, sender=Product)
def send_message(sender, instance, created, **kwargs):
    action = 'created' if created else 'updated'

    async_to_sync(get_channel_layer().group_send)(
        f"{instance.company.owner.id}-notifications", {"type": "send_last_message",
                                                       "text": f'{instance} {action}'}
    )
