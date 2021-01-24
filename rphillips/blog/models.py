from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    content = HTMLField()
    createdOn = models.DateField(auto_now_add=True)
    lastEdited = models.DateField(auto_now=True)

    def __str__(self):
        return 'Blog: ' + self.title
