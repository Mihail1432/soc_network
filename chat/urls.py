from django.urls import path
from . import views

urlpatterns = [
    # ваши остальные URL
    path('chat/<str:room_name>/', views.chat_room, name='chat'),
]
