# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-12 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0018_auto_20170912_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmtticket',
            name='choice',
            field=models.CharField(choices=[('dislike', 'dislike'), ('normal', 'normal'), ('like', 'like')], max_length=10),
        ),
        migrations.AlterField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(blank=True, default=3, null=True),
        ),
        migrations.AlterField(
            model_name='save',
            name='save_choice',
            field=models.CharField(choices=[('saved', 'saved'), ('save', 'save')], max_length=10),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(choices=[('dislike', 'dislike'), ('normal', 'normal'), ('like', 'like')], max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(blank=True, choices=[('girl', '女'), ('boy', '男'), ('secret', '保密')], max_length=10),
        ),
    ]
