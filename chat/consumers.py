import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Chat, Message
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_id = self.scope['url_route']['kwargs']['chat_id']
        self.room_group_name = f'chat_{self.chat_id}'

        # Присоединение к группе
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Отключение от группы
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Получение сообщения от WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        user_id = data['user_id']

        # Сохранение сообщения в базе данных
        user = await self.get_user(user_id)
        chat = await self.get_chat(self.chat_id)
        new_message = await self.save_message(chat, user, message)

        # Отправка сообщения в группу
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': new_message.content,
                'sender': user.username,
                'timestamp': str(new_message.timestamp)
            }
        )

    async def chat_message(self, event):
        # Отправка сообщения на WebSocket
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender'],
            'timestamp': event['timestamp']
        }))

    @staticmethod
    async def get_user(user_id):
        return await User.objects.get(id=user_id)

    @staticmethod
    async def get_chat(chat_id):
        return await Chat.objects.get(id=chat_id)

    @staticmethod
    async def save_message(chat, user, content):
        return await Message.objects.create(chat=chat, sender=user, content=content)
