# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-05 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0015_auto_20170825_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='save',
            name='save_choice',
            field=models.CharField(choices=[('save', 'save'), ('saved', 'saved')], max_length=10),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(choices=[('like', 'like'), ('normal', 'normal'), ('dislike', 'dislike')], max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='profile_image\\default.png', null=True, upload_to='profile_image'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(blank=True, choices=[('secret', '保密'), ('boy', '男'), ('girl', '女')], max_length=10),
        ),
        migrations.AlterField(
            model_name='video',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]