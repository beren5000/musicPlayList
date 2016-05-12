from django.contrib import admin
from applications.playList.models import PlayLists, Song

# Register your models here.
admin.site.register(PlayLists)
admin.site.register(Song)