# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-12 07:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firstapp', '0016_auto_20170905_1109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cmtticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('like', 'like'), ('dislike', 'dislike'), ('normal', 'normal')], max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='thisDislike',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='thisLike',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(choices=[('like', 'like'), ('dislike', 'dislike'), ('normal', 'normal')], max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(blank=True, choices=[('boy', '男'), ('secret', '保密'), ('girl', '女')], max_length=10),
        ),
        migrations.AddField(
            model_name='cmtticket',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_tickets', to='firstapp.Comment'),
        ),
        migrations.AddField(
            model_name='cmtticket',
            name='voter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cmtuser_tickets', to=settings.AUTH_USER_MODEL),
        ),
    ]
