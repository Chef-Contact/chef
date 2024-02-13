import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'chat'
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Обработка входящего сообщения от WebSocket клиента
        data_json = json.loads(text_data)
        message = data_json['message']

        # Сохранение сообщения в базе данных
        Message.objects.create(message=message)

        # Отправка сообщения обратно WebSocket клиенту
        await self.send(text_data=json.dumps({
            'message': message
        }))
