from django.shortcuts import render

# Decorators
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Forms
from .forms import UserForm, QualificationForm, ProfileForm
from django.forms.models import inlineformset_factory

from people.models import UserProfile, Qualification

def UserProfileFormView(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        qualification_form = QualificationForm(request.POST, instance=request.user.qualification)
        profile_form = ProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and qualification_form.is_valid() and profile_form.is_valid():
            user_form.save()
            qualification_form.save()
            profile_form.save()
    else:
        user_form = UserForm(instance=request.user)
        qualification_form = QualificationForm(request.POST, instance=request.user.qualification)
        profile_form = ProfileForm(instance=request.user.userprofile)
    return render(request, 'interaction_system/user_profile.html', {
        'user_form': user_form,
        'qualification_form': qualification_form,
        'profile_form': profile_form
    })
