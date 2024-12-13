from django.urls import path
from . import views

urlpatterns = [
    # ваши остальные URL
    path('chat/<int:room_id>/', views.chat_room, name='chat'),
]
