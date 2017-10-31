# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20170818_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='url_image',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='cover_image\\Desert.jpg', upload_to='profile_image'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='qq_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(choices=[('secret', '保密'), ('girl', '女'), ('boy', '男')], max_length=10),
        ),
    ]