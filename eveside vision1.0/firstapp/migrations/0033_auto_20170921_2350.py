# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-21 15:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0032_auto_20170920_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiXin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('createtime', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='cmtticket',
            name='choice',
            field=models.CharField(choices=[('dislike', 'dislike'), ('normal', 'normal'), ('like', 'like')], max_length=10),
        ),
        migrations.AlterField(
            model_name='save',
            name='save_choice',
            field=models.CharField(choices=[('save', 'save'), ('saved', 'saved')], max_length=10),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(choices=[('dislike', 'dislike'), ('normal', 'normal'), ('like', 'like')], max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(blank=True, choices=[('boy', '男'), ('secret', '保密'), ('girl', '女')], max_length=10),
        ),
        migrations.AddField(
            model_name='sixin',
            name='emiter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='myEmitSixin', to='firstapp.UserProfile'),
        ),
        migrations.AddField(
            model_name='sixin',
            name='getter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='myGetSixin', to='firstapp.UserProfile'),
        ),
    ]
