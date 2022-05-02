from django.db import models


class Schedule(models.Model):
    values = models.FloatField()
    time_create = models.DateTimeField(auto_now_add=True)
