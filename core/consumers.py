import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Group, ChatMessage

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_id = self.scope['url_route']['kwargs']['group_id']
        self.room_group_name = f'chat_{self.group_id}'
        
        # Check if user is authenticated and is member of the group
        if self.scope["user"].is_anonymous:
            await self.close()
            return
            
        is_member = await self.check_group_membership()
        if not is_member:
            await self.close()
            return
        
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
        
        # Save message to database
        await self.save_message(message)
        
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': self.scope["user"].username,
                'timestamp': timezone.now().strftime('%H:%M'),
            }
        )
    
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        timestamp = event.get('timestamp', str(timezone.now()))
        
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'timestamp': timestamp,
        }))
    
    @database_sync_to_async
    def check_group_membership(self):
        try:
            group = Group.objects.get(id=self.group_id)
            return (self.scope["user"] in group.members.all() or 
                   self.scope["user"] == group.created_by)
        except Group.DoesNotExist:
            return False
    
    @database_sync_to_async
    def save_message(self, message):
        try:
            group = Group.objects.get(id=self.group_id)
            ChatMessage.objects.create(
                group=group,
                user=self.scope["user"],
                message=message
            )
        except Group.DoesNotExist:
            pass
