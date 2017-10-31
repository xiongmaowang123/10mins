# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-25 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0012_auto_20170824_1913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='qq_number',
            new_name='phonenumber',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(choices=[('dislike', 'dislike'), ('normal', 'normal'), ('like', 'like')], max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='cover_image\\default.png', null=True, upload_to='profile_image'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(blank=True, choices=[('secret', '保密'), ('girl', '女'), ('boy', '男')], max_length=10),
        ),
    ]