from django.db import models
from field_history.tracker import FieldHistoryTracker

class Cow(models.Model):
    text_input = models.TextField(max_length=30)
    field_history = FieldHistoryTracker(['status'])
    def __str__(self):
        return self.text_input

