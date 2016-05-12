from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from applications.playList.models import Song


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('pk', 'name', 'description', 'song_file')