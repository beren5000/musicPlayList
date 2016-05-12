from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from applications.playList.models import Song
from applications.playList.serializers import SongSerializer


class SongsApiView(APIView):
    """
    List all Songs, or create a new Song.
    """
    def get(self, request, format=None, pk=None):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)