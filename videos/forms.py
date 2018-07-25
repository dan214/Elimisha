from django.forms import ModelForm, PasswordInput, Textarea, TextInput, FileInput,ImageField, ChoiceField, Select, ModelChoiceField

from .models import Video,Student, Profile

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.db import transaction


class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'document': FileInput(attrs={'class': 'form-control-file'}),
            'image': FileInput(attrs={'class': 'form-control-file'}),
            'quiz': Select(attrs={'class': 'form-control'}),
            'course': Select(attrs={'class': 'form-control'})
        }

class StudentSignUpForm(UserCreationForm):

    department = forms.CharField(widget = TextInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(widget = Textarea(attrs={'class': 'form-control'}))
    location = forms.CharField(widget = TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control'}))
    image = forms.FileField(widget = FileInput(attrs={'class': 'form-control-file'}))

    class Meta(UserCreationForm.Meta):
        model = Profile
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
        }

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.department = self.cleaned_data['department']
        user.bio = self.cleaned_data['bio']
        user.location = self.cleaned_data['location']
        user.image = self.cleaned_data['image']
        user.save()
        student = Student.objects.create(user=user)
        student.save()
        return user


class SpeakerSignUpForm(UserCreationForm):
    
    department = forms.CharField(widget = TextInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(widget = Textarea(attrs={'class': 'form-control'}))
    location = forms.CharField(widget = TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = Profile
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user