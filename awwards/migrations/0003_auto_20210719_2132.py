# Generated by Django 3.2.5 on 2021-07-19 18:32

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0002_auto_20210719_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='post'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='images'),
        ),
    ]
