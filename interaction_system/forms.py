from django import forms

from .models import UserProfile

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('user', 'location', 'birth_date', 'gender', 'highest_qualification', 'occupation', 'reading_frequency')
