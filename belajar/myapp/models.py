from django.db import models
from django.utils.translation import gettext as _


class GenreChoices(models.TextChoices):
    ACTION = "ACT", _("Action")
    DRAMA = "DRM", _("Drama")
    COMEDY = "COM", _("Comedy")


class MovieList(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=3, choices=GenreChoices.choices)
    year = models.IntegerField()
