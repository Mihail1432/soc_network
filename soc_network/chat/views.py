from django.shortcuts import render
from .models import Chat, get_obhe

def chat_list_view(request):
    chats = request.user.chats.all()  # Все чаты текущего пользователя
    return render(request, 'chat_list.html', {'chats': chats})

def chat_view(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    return render(request, 'chat.html', {
        'chat': chat,
    })