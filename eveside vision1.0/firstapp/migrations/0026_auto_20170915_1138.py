# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-15 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0025_auto_20170913_1225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='phonenumber',
            new_name='email',
        ),
        migrations.AlterField(
            model_name='save',
            name='save_choice',
            field=models.CharField(choices=[('saved', 'saved'), ('save', 'save')], max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(blank=True, choices=[('secret', '保密'), ('boy', '男'), ('girl', '女')], max_length=10),
        ),
    ]