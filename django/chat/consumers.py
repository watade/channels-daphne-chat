import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone

from .models import Room, Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]
        self.room_group_name = f"chat_{self.room_id}"
        self.room = await Room.objects.aget(public_id=self.room_id)
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_content = text_data_json["message"]
        message = await Message.objects.acreate(
            content=message_content,
            room_id=self.room.id,
            publisher_id=self.scope["user"].id,
        )
        await message.asave()
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat.message",
                "message": message_content,
                "publisher": self.scope["user"].username,
                "created_at": timezone.localtime(message.created_at).strftime(
                    "%Y/%m/%d %H:%M"
                ),
            },
        )

    async def chat_message(self, event):
        message = event["message"]
        publisher = event["publisher"]
        created_at = event["created_at"]
        await self.send(
            text_data=json.dumps(
                {"message": message, "publisher": publisher, "createdAt": created_at}
            )
        )
