from django import forms
from django.forms import fields, widgets
from django.forms.models import model_to_dict
from core.models import Post

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'image')
        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Caption this...'
            })
        }