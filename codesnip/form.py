from typing import Any
from django import forms
from .models import Codesnip

class CodesnipForm(forms.ModelForm):
    class Meta:
        model = Codesnip
        fields = ('title','text')
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control my-3' }),
            'text' : forms.Textarea(attrs={'class': 'form-control my-3' }),
        }
        labels = {
            'text': 'Write your thoughts'
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise forms.ValidationError('WE ONLY ACCEPT NOTES ABOUT DJANGO')
        return title