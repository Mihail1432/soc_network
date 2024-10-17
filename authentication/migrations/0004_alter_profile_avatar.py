# Generated by Django 5.1.1 on 2024-10-16 07:29

import authentication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_profile_birth_date_profile_cover_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='default_avatar.jpg', null=True, upload_to=authentication.models.user_directory_path),
        ),
    ]
