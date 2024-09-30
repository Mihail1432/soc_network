# Generated by Django 5.1 on 2024-09-30 09:22

import authentication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_remove_customuser_avatar_remove_customuser_bio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Birth date'),
        ),
        migrations.AddField(
            model_name='profile',
            name='cover_image',
            field=models.ImageField(blank=True, default='default_cover.png', null=True, upload_to=authentication.models.user_directory_path),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=30, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='default_avatar.png', null=True, upload_to=authentication.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500, verbose_name='Bio'),
        ),
    ]