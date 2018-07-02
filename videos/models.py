from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length= 400)
    document = models.FileField(upload_to='video_folder/')
