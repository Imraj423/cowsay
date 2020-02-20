from django.db import models
from django.utils import timezone


class Cow(models.Model):
    text_input = models.TextField(max_length=30)
    time = models.DateTimeField(default=timezone.now)
    default = 'default'
    satanic = 'satanic'
    ghostbusters = 'ghostbusters'
    sodomized = 'sodomized'
    dragon = 'dragon'
    CHOICE_LIST = [(satanic, 'satanic'), (ghostbusters, 'ghostbusters'),
                   (sodomized, 'sodomized'), (dragon, 'dragon')]
    cow_type = models.CharField(
        default=default, choices=CHOICE_LIST, max_length=12)
    
    def __str__(self):
        return self.text_input
