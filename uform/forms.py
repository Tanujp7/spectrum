from django import forms

from django.contrib.auth.models import User
from people.models import UserProfile, Qualification, PersonalDetails

class DateInput(forms.DateInput):
    input_type = 'date'

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
        fields = ('location', 'birth_date', 'gender', 'occupation', 'reading_frequency')
        widgets = {
            'birth_date': DateInput()
        }

class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = ('marital_status', 'no_of_kids', 'income', 'family_income')
