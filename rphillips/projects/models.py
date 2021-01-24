from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=120)
    description = HTMLField()
    repoLink = models.URLField()

    def __str__(self):
        return 'Project: ' + self.title

