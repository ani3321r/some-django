from django import forms
from .models import Xapp

class XForms(forms.ModelForm):
    class Meta:
        model = Xapp
        fields = ['text', 'photo']