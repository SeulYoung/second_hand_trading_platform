from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer, AsyncJsonWebsocketConsumer
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from chat_room.models import Communication
from django.contrib import auth

from account_app.models import MyUser


class ChatConsumer(AsyncJsonWebsocketConsumer):
    chats = dict()

    async def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        self.user = self.scope["user"]

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        # 添加用户至聊天组信息chats中
        try:
            ChatConsumer.chats[self.group_name].add(self)
        except:
            ChatConsumer.chats[self.group_name] = set([self])
        # 创建连接时调用
        await self.accept()

    async def disconnect(self, close_code):
        # 关闭连接调用
        # 将关闭的连接从群组中移除
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        # 将该客户端移除聊天组连接信息
        ChatConsumer.chats[self.group_name].remove(self)
        await self.close()

    async def receive_json(self, message, **kwargs):
        # 收到信息时调用
        websocket_id = message.get('websocket_id')
        to_user = message.get('to_user')
        from_user = message.get('from_user')
        time = message.get('time')
        # 信息发送
        length = len(ChatConsumer.chats[self.group_name])
        # if length == 2:
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chat.message",
                "message": message.get('message'),
                "from_user": from_user,
                "to_user": to_user,
                "time": time,
            },
        )
        if length < 2:
            # a = self.user.username
            # if a == to_user:
            mes = message.get('message')
            content = Communication.objects.filter(websocket_id=websocket_id)
            if content.exists():
                mes = content[0].content + '\n' + mes
                Communication.objects.filter(websocket_id=websocket_id, from_user=from_user, to_user=to_user).delete()
            Communication.objects.create(websocket_id=websocket_id, from_user=from_user, to_user=to_user, content=mes)

    # else:
    #     try:
    #         user = MyUser.objects.get(user_id=from_user)
    #     except MyUser.DoesNotExist:
    #         user = None
    #     from_username = MyUser.username
    #     await self.channel_layer.group_send(
    #         to_user,
    #         {
    #             "type": "push.message",
    #             "event": {
    #                 'message': message.get('message'),
    #                 'group': self.group_name,
    #                 'from_user': from_user,
    #                 'time': time,
    #                 'from_username': from_username,
    #             },
    #         },
    #     )

    async def chat_message(self, event):
        # 处理发送给我们的 “chat.message”事件
        await self.send_json({
            "message": event["message"],
            "from_user": event["from_user"],
            "to_user": event["to_user"],
            "time": event["time"],
        })


# 推送consumer
class PushConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['id']

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def push_message(self, event):
        # print(event)
        await self.send(text_data=json.dumps({
            "event": event['event']
        }))


def push(username, event):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        username,
        {
            "type": "push.message",
            "event": event
        }
    )

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name
#
#         # Join room group
#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )
#
#         await self.accept()
#
#     async def disconnect(self, close_code):
#         # Leave room group
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )
#
#     # Receive message from WebSocket
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#
#         # Send message to room group
#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )
#
#     # Receive message from room group
#     async def chat_message(self, event):
#         message = event['message']
#
#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({
#             'message': message
#         }))
