# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-12 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0017_auto_20170912_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmtticket',
            name='choice',
            field=models.CharField(choices=[('like', 'like'), ('normal', 'normal'), ('dislike', 'dislike')], max_length=10),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(choices=[('like', 'like'), ('normal', 'normal'), ('dislike', 'dislike')], max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(blank=True, choices=[('secret', '保密'), ('girl', '女'), ('boy', '男')], max_length=10),
        ),
    ]