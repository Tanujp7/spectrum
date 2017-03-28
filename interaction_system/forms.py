from django import forms

from .models import Location

class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ('city', 'state', 'country', 'continent',)
