from django import forms

from .models import Location

class LocationForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('city', 'state', 'country', 'continent',)
