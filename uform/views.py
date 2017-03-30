from django.shortcuts import render

# Decorators
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Forms
from .forms import UserForm, ProfileForm, PersonalDetailsForm, CareerForm
from django.forms.models import inlineformset_factory

from people.models import UserProfile, Career, PersonalDetails

@login_required
def UserProfileFormView(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
    return render(request, 'uform/user_profile.html', {
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
    return render(request, 'uform/user_personaldetails.html', {
        'personaldetails_form': personaldetails_form
    })

@login_required
def CareerFormView(request):
    if request.method == 'POST':
        career_form = CareerForm(request.POST, instance=request.user.career)
        if career_form.is_valid():
            career_form.save()
    else:
        career_form = CareerForm(instance=request.user.career)
    return render(request, 'uform/career.html', {
        'career_form': career_form,
    })
