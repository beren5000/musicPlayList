from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from utils.utils import Master

GRADE_CHOICES = (
    (0, _("0stars")),
    (1, _("1stars")),
    (2, _("2stars")),
    (3, _("3stars")),
    (4, _("4stars")),
    (5, _("5stars")),
)


# Create your models here.
class Stars(Master):
    grader = models.ForeignKey(User, verbose_name=_("grader"))
    grade = models.SmallIntegerField(choices=GRADE_CHOICES, verbose_name=_("grade"))

    class Meta:
        verbose_name = _("star")
        verbose_name_plural = _("stars")