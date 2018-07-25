from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_speaker = models.BooleanField(default=False)
    department = models.CharField(max_length=100,blank=True)
    bio = models.CharField(max_length=500,blank=True)
    location = models.CharField(max_length=30, blank=True)
    image = models.FileField(upload_to='video_folder/')

class Student(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE,related_name='profile',primary_key=True)

class Quiz(models.Model):
    name = models.CharField(max_length=200)
    document = models.FileField(upload_to='video_folder/')

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Video(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    document = models.FileField(upload_to='video_folder/')
    image = models.FileField(upload_to='video_folder/', default='/video_folder/nologo.png')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

