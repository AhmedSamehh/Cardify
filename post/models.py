from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30) # varchar
    description = models.TextField() #varchar max_length kbeeeeeeeeeeeeer
    likes = models.IntegerField()
    