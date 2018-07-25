from django.contrib import admin

from .models import Video, Quiz, Course, Student, Profile

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

admin.site.register(Video)
admin.site.register(Quiz)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Profile)