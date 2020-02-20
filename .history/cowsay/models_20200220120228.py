from django.db import models
from simple_history.models import HistoricalRecords


class Cow(models.Model):
    text_input = models.TextField(max_length=30)
    history = HistoricalRecords()
    
    def __str__(self):
        return self.text_input
