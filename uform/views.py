from django.shortcuts import render

# Decorators
from django.contrib.auth.models import Permission, User
from django.contrib.auth.decorators import login_required

# Forms
from .forms import UserForm, QualificationForm, ProfileForm
from django.forms.models import inlineformset_factory

def UserProfileFormView(request):
    LocationInlineFormSet = inlineformset_factory(Location, UserProfile, form=LocationForm)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        #location_form = LocationForm(request.POST, instance=request.user.location)
        #qualification_form = QualificationForm(request.POST, instance=request.user.qualification)
        profile_form = ProfileForm(request.POST, instance=request.user.userprofile)
        #if user_form.is_valid() and location_form.is_valid() and qualification_form.is_valid() and profile_form.is_valid():
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            #location_form.save()
            #qualification_form.save()
            profile_form.save()
    else:
        user_form = UserForm(instance=request.user)
        #location_form = LocationForm(request.POST, instance=request.user.location)
        #qualification_form = QualificationForm(request.POST, instance=request.user.qualification)
        profile_form = ProfileForm(instance=request.user.userprofile)
    return render(request, 'interaction_system/user_profile.html', {
        'user_form': user_form,
        #'location_form': location_form,
        #'qualification_form': qualification_form,
        'profile_form': profile_form
    })
