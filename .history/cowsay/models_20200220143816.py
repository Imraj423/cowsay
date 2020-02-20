from django.db import models
from django.utils import timezone


class Cow(models.Model):
    text_input = models.TextField(max_length=30)
    time = models.DateTimeField(default=timezone.now)
    sat = '-f satanic'
    gbs = '-f ghostbusters'
    eww = '-f sodomized'
    dra = '-f dragon'
    CHOICE_LIST = [(sat, '-f satanic'), (gbs, '-f ghostbusters'),
     (eww,  '-f sodomized'), (dra, '-f dragon')]

    def __str__(self):
        return self.text_input
