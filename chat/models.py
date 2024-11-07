from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Chat(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    is_group_chat = models.BooleanField(default=False)
    participants = models.ManyToManyField(User, related_name="chats")

    def __str__(self):
        return self.name if self.is_group_chat else f"Chat between {', '.join(user.username for user in self.participants.all())}"

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username}: {self.content[:50]}"
