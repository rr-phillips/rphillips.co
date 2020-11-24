from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    content = models.TextField()
    sentOn = models.DateTimeField(auto_now_add=True)

