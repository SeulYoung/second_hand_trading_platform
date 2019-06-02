from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer, AsyncJsonWebsocketConsumer
import json

from account_app.models import MyUser
from chat_app.models import ChatRoomMembers

ChatRoomMembers.objects.all().delete()


class ChatConsumer(AsyncJsonWebsocketConsumer):
    chats = dict()

    async def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        # self.room_group_name = 'chat_%s' % self.room_name
        #
        # self.user = self.scope["user"]
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
        to_user = message.get('to_user')
        from_user = message.get('from_user')
        time = message.get('time')
        # 信息发送
        length = len(ChatConsumer.chats[self.group_name])
        if length == 2:
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
        # else:
        #     try:
        #         user=

#     # verify if it's a legal user
#     if not isinstance(self.user, MyUser):
#         await self.disconnect(4000)
#         return
#
#     # Send message to room group
#     await self.channel_layer.group_send(
#         self.room_group_name,
#         {
#             'type': 'server_message',
#             'function': 'user in',
#             'user': self.user.username,
#         }
#     )
#
#     # user = await self.query_users(self.room_name)
#     # if not user:
#     self.add_user(self.room_name)
#
#     # Join room group
#     await self.channel_layer.group_add(
#         self.room_group_name,
#         self.channel_name
#     )
#
#     await self.accept()
#
# async def disconnect(self, close_code):
#     # Leave room group
#     self.remove_user(self.room_name)
#     await self.channel_layer.group_discard(
#         self.room_group_name,
#         self.channel_name
#     )
#
#     await self.channel_layer.group_send(
#         self.room_group_name,
#         {
#             'type': 'server_message',
#             'function': 'user out',
#             'user': self.user.username,
#         }
#     )
#
# # Receive message from WebSocket
# async def receive(self, text_data):
#     text_data_json = json.loads(text_data)
#     message = text_data_json['message']
#
#     # Send message to room group
#     await self.channel_layer.group_send(
#         self.room_group_name,
#         {
#             'type': 'chat_message',
#             'user': self.user.username,
#             'message': message
#         }
#     )
#
# # Receive message from room group
# async def chat_message(self, event):
#     # Send message to WebSocket
#     await self.send(text_data=json.dumps({
#         'type': 'message',
#         'user': event['user'],
#         'message': event['message'],
#     }))
#
# # Receive message from room group
# async def server_message(self, event):
#     func = event['function']
#     if func == 'user in':
#         username = event['user']
#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({
#             'type': func,
#             'user': username,
#         }))
#     elif func == 'user out':
#         username = event['user']
#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({
#             'type': func,
#             'user': username,
#         }))
#
# # @database_sync_to_async0
# def add_user(self, room_name):
#     return ChatRoomMembers.objects.create(room_name=room_name, user=self.user)
#
# # @database_sync_to_async
# def remove_user(self, room_name):
#     return ChatRoomMembers.objects.filter(room_name=room_name, user_id=self.user.username).delete()
#
# @database_sync_to_async
# def query_users(self, room_name):
#     return ChatRoomMembers.objects.filter(room_name=room_name).all()
