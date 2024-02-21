from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import ChatRoom, Message

@login_required
def chatrooms(request):
    chatrooms = ChatRoom.objects.all()

    return render(request, 'chat_room/chatrooms.html', {'chatrooms': chatrooms})

@login_required
def chatroom(request, slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    messages = Message.objects.filter(chatroom=chatroom)

    return render(request, 'chat_room/chatroom.html', {'chatroom': chatroom, 'messages': messages})