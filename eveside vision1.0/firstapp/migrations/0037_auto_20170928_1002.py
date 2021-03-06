# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-28 02:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0036_auto_20170927_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='dongTaiNum',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cmtticket',
            name='choice',
            field=models.CharField(choices=[('like', 'like'), ('normal', 'normal'), ('dislike', 'dislike')], max_length=10),
        ),
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
    ]
