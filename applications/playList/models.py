from __future__ import unicode_literals
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.text import slugify
from utils.utils import Master
from django.utils.translation import ugettext_lazy as _

from django.db import models


class PlayLists(Master):
    user = models.ForeignKey(User, blank=False, null=False, verbose_name=_("user"))
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name=_("name"))
    songs = models.ManyToManyField('Song', blank=True, related_name="%(app_label)s_%(class)s_songs",
                                   verbose_name=_("songs"))
    is_private = models.BooleanField(default=False, blank=False, null=False, verbose_name=_("is_private"))

    class Meta:
        verbose_name = _("playlist")
        verbose_name_plural = _("playlists")


# function to return the correct UPLOAD_TO variable for the song field.
# All the songs are storage in the folder with the name of the profile
def song_name(instance, filename):
    filename = filename.split('.')
    filename = str(instance.pk)+datetime.now().strftime("-%Y-%m-%d-%H-%M-%S")+str('.')+str(filename[-1])
    return '/'.join(['song', slugify(instance.name), filename])


class Song(Master):
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name=_("name"))
    song_file = models.FileField(blank=True, upload_to=song_name, verbose_name=_("song_file"))

    class Meta:
        verbose_name = _("song")
        verbose_name_plural = _("songs")