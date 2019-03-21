from django.db import models

class FeedbackData(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    date = models.DateField(max_length=100)
    location = models.CharField(max_length=100)
    feedback = models.TextField(max_length=1000)
