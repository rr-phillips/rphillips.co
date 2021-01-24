from django.db import models
import datetime
from tinymce.models import HTMLField

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=150)
    description = HTMLField()
    company = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return 'Job: ' + self.title + ' - ' + self.company

class Education(models.Model):
    degree = models.CharField(max_length=150)
    institution = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return 'Education: ' + self.degree + ' - ' + self.institution
