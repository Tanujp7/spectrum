from django.shortcuts import render

# Decorators
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Forms
from .forms import UserForm, QualificationForm, ProfileForm, PersonalDetailsForm, OccupationForm
from django.forms.models import inlineformset_factory

from people.models import UserProfile, Qualification, PersonalDetails

@login_required
def UserProfileFormView(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and qualification_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
    return render(request, 'interaction_system/user_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def PersonalDetailsFormView(request):
    if request.method == 'POST':
        personaldetails_form = PersonalDetailsForm(request.POST, instance=request.user.personaldetails)
        if personaldetails_form.is_valid():
            personaldetails_form.save()
    else:
        personaldetails_form = PersonalDetailsForm(instance=request.user.personaldetails)
    return render(request, 'interaction_system/user_personaldetails.html', {
        'personaldetails_form': personaldetails_form
    })

@login_required
def CareerFormView(request):
    if request.method == 'POST':
        qualification_form = QualificationForm(request.POST, instance=request.user.qualification)
        occupation_form = OccupationForm(request.POST, instance=request.user.userprofile)
        if qualification_form.is_valid() and occupation_form.is_valid():
            occupation_form.save()
            qualification_form.save()
    else:
        qualification_form = QualificationForm(instance=request.user.qualification)
        occupation_form = OccupationForm(instance=request.user.userprofile)
    return render(request, 'interaction_system/career.html', {
        'qualification_form': qualification_form,
        'occupation_form': occupation_form
    })
