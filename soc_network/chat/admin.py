from django.contrib import admin
from .models import Chat, Message
# Register your models here.
@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    pass
