# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-22 04:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firstapp', '0004_auto_20170819_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.CharField(default='static/images/default.png', max_length=250)),
                ('comment', models.TextField(blank=True, null=True)),
                ('createtime', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Save',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('save_choice', models.BooleanField(default=False)),
                ('saver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_saves', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('normal', 'normal'), ('like', 'like'), ('dislike', 'dislike')], max_length=10)),
            ],
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='name',
            new_name='nickname',
        ),
        migrations.AddField(
            model_name='video',
            name='createtime',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(choices=[('girl', '女'), ('boy', '男'), ('secret', '保密')], max_length=10),
        ),
        migrations.AddField(
            model_name='ticket',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_tickets', to='firstapp.Video'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='voter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_tickets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='save',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_saves', to='firstapp.Video'),
        ),
        migrations.AddField(
            model_name='comment',
            name='belong_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='under_comments', to='firstapp.Video'),
        ),
        migrations.AddField(
            model_name='comment',
            name='commenter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]