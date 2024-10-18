from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from .models import Chat, Message
from authentication.models import CustomUser

def create_chat(request, username):
    other_username = get_object_or_404(CustomUser, username=username)
    chat = Chat.objects.filter(participants=request.user).filter(participants=other_username).first()
    chats = Chat.objects.filter(participants=request.user)

    if not chat:
        chat = Chat.objects.create()
        chat.participants.add(request.user, other_username)

    return JsonResponse({'chat_id': chat.id})


def chat_list(request):
    chats = Chat.objects.filter(participants=request.user)
    return render(request, 'chats/chat_list.html', {'chats': chats})


def chat_detail(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id, participants=request.user)
    messages = Message.objects.filter(chat_id=chat_id).select_related('sender')
    messages_data = [{'content': message.content, 'sender__username': message.sender.username} for message in messages]
    return JsonResponse(list(messages), safe=False)

def send_message(request, chat_id):
    if request.method == "POST":
        chat = get_object_or_404(Chat, id=chat_id, participants=request.user)
        message_content = request.POST.get('message')
        Message.objects.create(chat=chat, sender=request.user, content=message_content)
        return JsonResponse({'status': 'Message sent!'})