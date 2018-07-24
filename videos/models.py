from django.db import models
from django.contrib.auth.models import User, AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='userprofile')
    department = models.CharField(max_length=100)
    bio = models.CharField(max_length=500,blank=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

class Quiz(models.Model):
    name = models.CharField(max_length=200)
    document = models.FileField(upload_to='video_folder/')

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    speaker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Video(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    document = models.FileField(upload_to='video_folder/')
    image = models.FileField(upload_to='video_folder/', default='/video_folder/nologo.png')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

