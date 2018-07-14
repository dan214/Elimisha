from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    name = models.CharField(max_length=200)
    document = models.FileField(upload_to='video_folder/')

    def __str__(self):
        return self.name

class Video(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length= 400)
    document = models.FileField(upload_to='video_folder/')
    image = models.FileField(upload_to='video_folder/', default='/video_folder/nologo.png')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,null=True, blank=True)
    speaker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

