from django import forms
from .models import CarVariety

class CarVarietyForm(forms.Form):
    car_variety = forms.ModelChoiceField(queryset=CarVariety.objects.all(), label="Select a car variety")