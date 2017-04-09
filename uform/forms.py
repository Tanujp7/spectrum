from django import forms

from django.contrib.auth.models import User
from people.models import UserProfile, Career, PersonalDetails, Hobbies, Interest

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class HobbiesForm(forms.ModelForm):
    class Meta:
        model = Hobbies
        fields = ('working_hrs', 'family_hrs', 'own_hrs', 'reading_frequency')
        help_texts = {
                'working_hrs': ('Time in Hours'),
                'family_hrs': ('Time in Hours'),
                'own_hrs': ('Time in Hours'),
        }

class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ('qualification_name', 'qualification_stream', 'occupation')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('location', 'birth_date', 'gender')
        help_texts = {
                'birth_date': ('Date should be of the format yyyy-mm-dd ; ex: 1994-03-31'),
        }
        widgets = {
            'gender': forms.RadioSelect(),
        }

class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = ('marital_status', 'no_of_kids')
        widgets = {
            'marital_status': forms.RadioSelect(),
        }
        
class InterestForm(forms.ModelForm):
    interest_keywords = forms.ModelMultipleChoiceField(label="Tell us Something about your Interests", widget=forms.CheckboxSelectMultiple(),required=False, queryset=Interest.objects.all())
    class Meta:
        model = UserProfile
        fields = ('interest_keywords',)
