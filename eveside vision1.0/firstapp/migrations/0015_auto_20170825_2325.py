# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-25 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0014_auto_20170825_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='save',
            name='save_choice',
            field=models.CharField(choices=[('saved', 'saved'), ('save', 'save')], max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(blank=True, choices=[('boy', '男'), ('girl', '女'), ('secret', '保密')], max_length=10),
        ),
    ]
