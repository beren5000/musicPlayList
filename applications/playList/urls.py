from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from applications.playList.views import SongsApiView, PlaylistApiView

urlpatterns = [
    url(r'^songs/', SongsApiView.as_view()),
    url(r'^playlists/', PlaylistApiView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)