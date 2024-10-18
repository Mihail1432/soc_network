from django.contrib import admin
from .models import Profile  # Импорт модели Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio']
