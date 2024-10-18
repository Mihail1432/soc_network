from django.urls import path
from . import views

urlpatterns = [
    path('chats/', views.chat_list, name='chat_list'),  # Список всех чатов
    path('chats/<int:chat_id>/', views.chat_detail, name='chat_detail'),  # Детализация чата
    path('chats/<int:chat_id>/send/', views.send_message, name='send_message'),  # Отправка сообщения
    path('profile/<str:username>/create_chat/', views.create_chat, name='create_chat'),  # Создание чата в профиле пользователя
]
