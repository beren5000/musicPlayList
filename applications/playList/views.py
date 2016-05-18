from django.contrib.auth.models import User
from django.shortcuts import render
import jwt
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from applications.playList.models import Song, PlayLists
from applications.playList.serializers import SongSerializer, PlaylistSerializer
from rest_framework_jwt.utils import jwt_decode_handler


class SongsApiView(APIView):
    """
    List all Songs, or create a new Song.
    """
    permission_classes = (AllowAny,)
    def get(self, request, format=None, pk=None):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)


@authentication_classes([JSONWebTokenAuthentication,  SessionAuthentication])
class PlaylistApiView(APIView):
    """
    List all Songs, or create a new Song.
    """
    def get(self, request, format=None, pk=None):
        if request.user.is_authenticated():
            user_id = request.user.pk
        else:
            try:
                token = request.META['HTTP_AUTHORIZATION'][3:]
                decode = jwt_decode_handler(token)
                user_id = decode['user_id']
            except KeyError:
                return Response({"detail": "Authorization Token not provided or user Not Authenticated"}, status=401)
        playlists = PlayLists.objects.filter(user__pk=user_id)
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data)

    def put(self, request, format=None, pk=None):
        if request.user.is_authenticated():
            user_id = request.user.pk
        else:
            try:
                token = request.META['HTTP_AUTHORIZATION'][3:]
                decode = jwt_decode_handler(token)
                user_id = decode['user_id']
            except KeyError:
                return Response({"detail": "Authorization Token not provided or user Not Authenticated"}, status=401)
        user = User.objects.get(pk=user_id);
        name = request.POST['name']
        description = request.POST['description']
        songs = request.POST.getlist('songs[]')
        songs = Song.objects.filter(pk__in=songs)
        playlist = PlayLists(user=user, name=name, description=description)
        playlist.save()
        playlist.songs.add(*songs)
        playlist.save()
        return Response({"inserted": playlist.pk}, status=200)