# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 01:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayLists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='description')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
            ],
            options={
                'verbose_name': 'playlist',
                'verbose_name_plural': 'playlists',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='description')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('song_file', models.FileField(blank=True, upload_to=b'', verbose_name='song_file')),
            ],
            options={
                'verbose_name': 'song',
                'verbose_name_plural': 'songs',
            },
        ),
        migrations.AddField(
            model_name='playlists',
            name='songs',
            field=models.ManyToManyField(blank=True, related_name='playlist_playlists_songs', to='playList.Song', verbose_name='songs'),
        ),
        migrations.AddField(
            model_name='playlists',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
