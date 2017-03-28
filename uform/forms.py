from django import forms

from django.contrib.auth.models import User
from people.models import UserProfile, Qualification

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class QualificationForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = ('qualification_name', 'qualification_stream')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('birth_date', 'gender', 'occupation', 'reading_frequency')
