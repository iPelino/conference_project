# forms.py
from django import forms
from .models import Conference

class ConferenceForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ['name', 'description', 'topic', 'date', 'location']
