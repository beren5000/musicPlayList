from django.shortcuts import render
import jwt
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


@authentication_classes([JSONWebTokenAuthentication,])
class PlaylistApiView(APIView):
    """
    List all Songs, or create a new Song.
    """
    def get(self, request, format=None, pk=None):
        try:
            token = request.META['HTTP_AUTHORIZATION'][3:]
            decode = jwt_decode_handler(token)
            user_id = decode['user_id']
        except KeyError:
            return Response({"detail":"Authorization Token not provided"}, status=401)
        playlists = PlayLists.objects.filter(user__pk=user_id)
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data)