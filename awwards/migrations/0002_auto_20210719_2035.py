# Generated by Django 3.2.5 on 2021-07-19 17:35

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=cloudinary.models.CloudinaryField(default='default.png', max_length=255, verbose_name='post/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(default='default.png', max_length=255, verbose_name='images/'),
        ),
    ]