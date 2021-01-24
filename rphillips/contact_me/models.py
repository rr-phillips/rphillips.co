from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    content = HTMLField()
    sentOn = models.DateTimeField(auto_now_add=True)

