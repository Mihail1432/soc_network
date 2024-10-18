from django.db import models
from django.conf import settings

class Chat(models.Model):
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='chats')
    created_at = models.DateTimeField(auto_now_add=True)



    @property
    def other_username(self):
        return self.participants.exclude(id=self.participants.first().id).first().username

        
    def __str__(self):
        return f"Chat between: {', '.join([user.username for user in self.participants.all()])}"

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username}"
