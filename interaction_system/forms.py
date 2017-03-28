from django import forms

from .models import UserProfile, User, Location, Qualification

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('city', 'state', 'country', 'continent')

class QualificationForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = ('qualification_name', 'qualification_stream')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('birth_date', 'gender', 'occupation', 'reading_frequency')
