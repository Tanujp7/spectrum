from django import forms

from django.contrib.auth.models import User
from people.models import UserProfile, Career, PersonalDetails, Hobbies, Interest

class DateInput(forms.DateInput):
    input_type = 'date'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class HobbiesForm(forms.ModelForm):
    class Meta:
        model = Hobbies
        fields = ('working_hrs', 'family_hrs', 'own_hrs', 'reading_frequency')

class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ('qualification_name', 'qualification_stream', 'occupation')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('location', 'birth_date', 'gender')
        widgets = {
            'birth_date': DateInput()
        }

class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = ('marital_status', 'no_of_kids', 'income', 'family_income')

class InterestForm(forms.ModelForm):
    keyword = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(),required=False)
    class Meta:
        model = Interest
        fields = ('keyword',)
