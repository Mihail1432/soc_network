from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Требование уникального email




def user_directory_path(instance, filename):
    # Файлы будут загружаться в MEDIA_ROOT/user_<id>/<filename>
    return f'user_{instance.user.id}/{filename}'

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=user_directory_path, default='default_avatar.png', blank=True, null=True)
    cover_image = models.ImageField(upload_to=user_directory_path, default='default_cover.png', blank=True, null=True)
    bio = models.TextField(_("Bio"), max_length=500, blank=True)
    location = models.CharField(_("Location"), max_length=30, blank=True)
    birth_date = models.DateField(_("Birth date"), null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'