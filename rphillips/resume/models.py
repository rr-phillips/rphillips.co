from django.db import models
import datetime

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    company = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    start = models.DateTimeField(default=datetime.date.today)
    end = models.DateTimeField(null=True, blank=True)

class Education(models.Model):
    degree = models.CharField(max_length=150)
    institution = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)

