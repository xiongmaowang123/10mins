# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-04 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0042_auto_20171003_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='thisCmt',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='thisDislike',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='thisLike',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='thisRpl',
        ),
        migrations.AlterField(
            model_name='cmtticket',
            name='choice',
            field=models.CharField(choices=[('like', 'like'), ('dislike', 'dislike'), ('normal', 'normal')], max_length=10),
        ),
        migrations.AlterField(
            model_name='save',
            name='save_choice',
            field=models.CharField(choices=[('save', 'save'), ('saved', 'saved')], max_length=10),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(choices=[('like', 'like'), ('dislike', 'dislike'), ('normal', 'normal')], max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(blank=True, choices=[('secret', '保密'), ('girl', '女'), ('boy', '男')], max_length=10),
        ),
    ]
