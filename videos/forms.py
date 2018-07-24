from django.forms import ModelForm, Textarea, TextInput, FileInput,ImageField, ChoiceField, Select, ModelChoiceField
from django.contrib.auth.models import User
from .models import Video,Student

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


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


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('department', 'bio','location')

    
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','password1', 'password2',)



class SignUpForm(UserCreationForm):

    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    bio = forms.CharField()
    department = forms.CharField()
    location = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'birth_date', 'bio' ,'department','location' )