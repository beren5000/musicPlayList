from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from applications.playList.views import SongsApiView

urlpatterns = [
    url(r'^songs/', SongsApiView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)