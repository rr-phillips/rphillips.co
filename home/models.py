from django.db import models
import datetime
from tinymce.models import HTMLField

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=120)
    description = HTMLField()
    repoLink = models.URLField()

    def __str__(self):
        return 'Project: ' + self.title

class Job(models.Model):
    title = models.CharField(max_length=150)
    description = HTMLField()
    company = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    start = models.DateField()
    end = models.DateField(null=True, blank=True)

    def __str__(self):
        return 'Job: ' + self.title + ' - ' + self.company

class Education(models.Model):
    degree = models.CharField(max_length=150)
    institution = models.CharField(max_length=200)
    start = models.DateField()
    end = models.DateField(null=True, blank=True)

    def __str__(self):
        return 'Education: ' + self.degree + ' - ' + self.institution
