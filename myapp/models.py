from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    title=models.TextField(max_length=100)
    body=models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)

class PostPic(models.Model):
    myimage=models.ImageField(upload_to='images', default="null")
    desc=models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)

class PostFile(models.Model):
    myfile=models.FileField(upload_to='files',blank=False, null=False)
    desc=models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)

