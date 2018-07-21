from django.forms import ModelForm, Textarea, TextInput, FileInput,ImageField, ChoiceField, Select, ModelChoiceField
from .models import Video

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
