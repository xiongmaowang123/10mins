# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-18 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(choices=[('secret', '保密'), ('girl', '女'), ('boy', '男')], max_length=10),
        ),
    ]