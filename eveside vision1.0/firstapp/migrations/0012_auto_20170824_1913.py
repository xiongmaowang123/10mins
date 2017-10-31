# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-24 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0011_auto_20170824_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='save',
            name='save_choice',
            field=models.CharField(choices=[('saved', 'saved'), ('save', 'save')], max_length=10),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(choices=[('like', 'like'), ('dislike', 'dislike'), ('normal', 'normal')], max_length=10),
        ),
    ]
