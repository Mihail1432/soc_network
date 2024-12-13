from django.contrib.auth import get_user_model
from django.db import models

from authentication.models import CustomUser

User = get_user_model()

class Chat(models.Model):
    unique_id = models.AutoField(primary_key=True)  # Автоинкрементируемое уникальное поле
    is_group_chat = models.BooleanField(default=False)
    participants = models.ManyToManyField(User, related_name="chats")

    def __str__(self):
        if self.is_group_chat:
            return f"Group Chat #{self.unique_id}"
        else:
            participants = ', '.join(CustomUser.username for user in self.participants.all())
            return f"Chat #{self.unique_id} between {participants}"
class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username}: {self.content[:50]}"
