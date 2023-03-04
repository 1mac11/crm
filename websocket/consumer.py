from django.contrib.auth.models import AnonymousUser

import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from websocket.models import Notifications


class Consumer(AsyncWebsocketConsumer):
    groups = ["general"]

    async def connect(self):
        await self.accept()
        if not isinstance(self.scope['user'], AnonymousUser):
            self.user_id = self.scope["user"].id
            await self.channel_layer.group_add(f"{self.user_id}-notifications", self.channel_name)
            await self.send_all_unread_notifications()
        else:
            await self.send(text_data=json.dumps('send request with token pls'))
            await self.close()

    async def send_last_message(self, event):
        last_msg = await self.get_last_notification(self.user_id)
        await self.send(text_data=json.dumps(last_msg))

    async def send_all_unread_notifications(self):
        last_msg = await self.get_all_unread_notifications(self.user_id)
        await self.send(text_data=json.dumps(last_msg))

    @database_sync_to_async
    def get_last_notification(self, user_id):
        notification = Notifications.objects.filter(read_status=False, company__owner__id=user_id).last()
        data = {'last change': {'title': notification.title,
                                'description': notification.description,
                                'company': notification.company.name,
                                'time': str(notification.created_time),
                                'read_status': notification.read_status}}
        return data

    @database_sync_to_async
    def get_all_unread_notifications(self, user_id):
        notifications = Notifications.objects.filter(read_status=False, company__owner__id=user_id)
        data = {}
        k = 1

        for i in notifications:
            data[k] = {'title': i.title,
                       'description': i.description,
                       'company': i.company.name,
                       'time': str(i.created_time),
                       'read_status': i.read_status}
            k += 1

        if data:
            return data
        else:
            return f'no unread notifications for user with id {user_id}'
