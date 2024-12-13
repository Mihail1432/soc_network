from django.shortcuts import render, get_object_or_404
from .models import Chat

def chat_room(request, room_id):
    chat = get_object_or_404(Chat, unique_id=room_id)
    return render(request, 'chat/room.html', {
        'chat': chat,
        'user': request.user
    })