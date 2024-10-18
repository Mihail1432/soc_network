from django.urls import path
from . import views
from authentication.views import user_profile_view



urlpatterns = [
    path('chats/', views.chat_list_view, name='chat_list'),
    path('chat/<int:chat_id>/', views.chat_detail_view, name='chat_detail'),
    path('chat/<int:chat_id>/send/', views.send_message_view, name='send_message'),
    path('profile/<str:username>/', user_profile_view, name='profile'),
]
