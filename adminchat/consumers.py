import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async
from .models import ChatMessage


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        self.room_name = self.scope['url_route']['kwargs'].get('room_name')
        self.user = self.scope['user']

        if not self.user.is_superuser:
            self.room_name = f'user_{self.user.username}'

        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        await self.load_history(self.room_name)


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        receiver = await self.get_receiver()

        await self.save_message(self.user, receiver, message, self.room_name)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'username': self.user.username,
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'username': username,
            'message': message
        }))

    @sync_to_async
    def save_message(self, sender, receiver, message, room_name):
        return ChatMessage.objects.create(
            sender=sender,
            receiver=receiver,
            message=message,
            room_name=room_name
        )

    @sync_to_async
    def get_receiver(self):
        return User.objects.filter(is_superuser=True).first()

    async def load_history(self, room_name):
        messages = await self.get_last_messages(room_name, 50)
        async for message in messages:
            await self.send(text_data=json.dumps({
                'message': message.message,
                'username': message.sender.username,
                'timestamp': message.timestamp.isoformat(),
            }))

    @sync_to_async
    def get_last_messages(self, room_name, limit):
        return ChatMessage.objects.filter(room_name=room_name).order_by('timestamp')[:limit].select_related("sender")
