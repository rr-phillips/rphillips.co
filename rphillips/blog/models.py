from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField();
    createdOn = models.DateField(auto_now_add=True)
    lastEdited = models.DateField(auto_now=True)
