from django.contrib import admin
from .models import Comment, Like, Post  # Добавьте другие модели


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)