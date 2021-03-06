from django.db import models
from django.utils import timezone


class Cow(models.Model):
    text_input = models.TextField(max_length=30)
    time = models.DateTimeField(default=timezone.now)
    '' = cow
    '-f satanic' = sat
    '-f ghostbusters' = gbs
    '-f sodomized' = eww
    '-f dragon' = dra
    CHOICE_LIST = [(sat, '-f satanic'), (gbs, '-f ghostbusters'),
                   (eww,  '-f sodomized'), (dra, '-f dragon')]
    cow_type = models.CharField(
        default=cow, choices=CHOICE_LIST, max_length=15)

    def __str__(self):
        return self.text_input
