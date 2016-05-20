from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from applications.playList.models import Song, PlayLists


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('pk', 'name', 'description', 'star_ranking',  'song_file')


class PlaylistSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = PlayLists
        fields = ('pk', 'user', 'name', 'description', 'is_private', 'songs')