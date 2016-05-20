from __future__ import unicode_literals
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.text import slugify

from applications.ranking.models import Stars
from utils.utils import Master
from django.utils.translation import ugettext_lazy as _

from django.db import models


class PlayLists(Master):
    user = models.ForeignKey(User, blank=False, null=False, verbose_name=_("user"))
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name=_("name"))
    songs = models.ManyToManyField('Song', blank=True, related_name="%(app_label)s_%(class)s_songs",
                                   verbose_name=_("songs"))
    is_private = models.BooleanField(default=False, blank=False, null=False, verbose_name=_("is_private"))

    def __unicode__(self):
        return str(self.pk) + ": " + self.user.username + " - " + self.name

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
    stars = models.ManyToManyField(Stars, blank=True, related_name="%(app_label)s_%(class)s_stars",
                                   verbose_name=_("stars"))
    star_ranking = models.FloatField(default=0, verbose_name=_("star_ranking"))

    def __unicode__(self):
        return str(self.pk) + " - " + self.name

    class Meta:
        verbose_name = _("song")
        verbose_name_plural = _("songs")

    def save(self, *args, **kwargs):
        try:
            if self.stars.all().count() > 0:
                self.star_ranking = self.stars_rank_number
        except:
            self.star_ranking = 1
        super(Song, self).save(*args, **kwargs)

    @property
    def stars_rank_number(self):
        """
        formula for ranking
        sumatoria de (multiplicacion de la estrella por el numero de votos por esa estrella) sobre el total de votos
        """
        stars = self.stars.all()
        star_1 = float(stars.filter(grade=1).count() * 1)
        star_2 = float(stars.filter(grade=2).count() * 2)
        star_3 = float(stars.filter(grade=3).count() * 3)
        star_4 = float(stars.filter(grade=4).count() * 4)
        star_5 = float(stars.filter(grade=5).count() * 5)
        try:
            ranking = float(star_1 + star_2 + star_3 + star_4 + star_5) / float(stars.count())
        except:
            ranking = 0
        return ranking

    @property
    def stars_rank(self):
        resp = []
        for i in range(int(self.star_ranking)):
            resp += [1]
        for i in range(5 - len(resp)):
            resp += [0]
        return resp