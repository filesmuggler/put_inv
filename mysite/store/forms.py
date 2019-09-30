from django import forms

from .models import Part

class PostForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ('name','text','total_number')