# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-20 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0029_auto_20170920_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmtticket',
            name='choice',
            field=models.CharField(choices=[('normal', 'normal'), ('dislike', 'dislike'), ('like', 'like')], max_length=10),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(choices=[('normal', 'normal'), ('dislike', 'dislike'), ('like', 'like')], max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(blank=True, choices=[('boy', '男'), ('secret', '保密'), ('girl', '女')], max_length=10),
        ),
    ]