from django.db import models


class Cow(models.Model):
    text_input = models.TextField(max_length=30)

    def __str__(self):
        return self.text_input
