import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

        # Найдите чат по chat_id
        chat = await self.get_chat(self.chat_id)
        sender = await self.get_user(sender_id)

        # Сохранение сообщения в базе данных
        await self.create_message(chat, sender, message)
        # Сохраним сообщение в базу данных
        sender = User.objects.get(id=sender_id)
        Message.objects.create(chat=chat, sender=sender, content=message)

        # Отправка сообщения обратно в группу чата
        await self.channel_layer.group_send(
            self.chat_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender.username,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        # Отправить сообщение в WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
        }))

    @database_sync_to_async
    def get_chat(self, chat_id):
        return Chat.objects.get(id=chat_id)

    @database_sync_to_async
    def get_user(self, user_id):
        return User.objects.get(id=user_id)

    @database_sync_to_async
    def create_message(self, chat, sender, message):
        return Message.objects.create(chat=chat, sender=sender, content=message)


def connect(self):
    self.chat_id = self.scope['url_route']['kwargs']['chat_id']
    self.room_group_name = f'chat_{self.chat_id}'

    # Присоединяем пользователя к группе чата
    async_to_sync(self.channel_layer.group_add)(
        self.room_group_name,
        self.channel_name
    )

    self.accept()

    # Отправка истории сообщений при подключении
    chat = Chat.objects.get(id=self.chat_id)
    messages = chat.messages.all()

    for message in messages:
        self.send(text_data=json.dumps({
            'message': message.content,
            'sender': message.sender.username,
            'timestamp': str(message.timestamp),
        }))