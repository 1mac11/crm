import asyncio
import json

from asgiref.sync import sync_to_async, async_to_sync
from channels.consumer import AsyncConsumer
from random import randint
from time import sleep

from channels.db import database_sync_to_async
from channels.generic.websocket import WebsocketConsumer

from websocket.models import Notifications


class PracticeConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        # when websocket connects
        print("connected", event)

        await self.send({"type": "websocket.accept"})
        await self.channel_layer.group_add('notifications', self.channel_name)
        await self.send_unread_notifications()

    async def product_changed(self, event):
        print(event)
        await self.send_unread_notifications()

    async def send_unread_notifications(self):
        @database_sync_to_async
        def get_unread_notifications():
            notifications = Notifications.objects.filter(read_status=False)
            data = ''
            line = '<br/><br/>'

            for i in notifications:
                data += f'[ {str(i)} ]{line}'

            return data

        await self.send({
            "type": "websocket.send",
            "text": json.dumps(
                await get_unread_notifications(),
            )
        })

    async def websocket_receive(self, event):
        # when messages is received from websocket
        print("receive", event)

    async def websocket_disconnect(self, event):
        # when websocket disconnects
        print("disconnected", event)

