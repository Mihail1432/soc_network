from django.urls import path
from  . import consumers
from django.urls import re_path
from .consumers import ChatConsumer




websocket_urlpatterns = [
    path('ws/chat/<str:chat_id>/', consumers.ChatConsumer.as_asgi()),
]


def get_websocket_urlpatterns():
    return [
        re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
    ]

websocket_urlpatterns = get_websocket_urlpatterns()