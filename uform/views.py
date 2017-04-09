from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Decorators
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Forms
from .forms import UserForm, ProfileForm, PersonalDetailsForm, CareerForm, HobbiesForm, InterestForm
from django.forms.models import inlineformset_factory

from people.models import UserProfile, Career, PersonalDetails, Hobbies, Interest

@login_required
def UserProfileFormView(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('PersonalDetailsFormView'))
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
        hobbies_form = HobbiesForm(request.POST, instance=request.user.hobbies)
        if personaldetails_form.is_valid() and hobbies_form.is_valid():
            personaldetails_form.save()
            hobbies_form.save()
            return HttpResponseRedirect(reverse('CareerFormView'))
    else:
        personaldetails_form = PersonalDetailsForm(instance=request.user.personaldetails)
        hobbies_form = HobbiesForm(instance=request.user.hobbies)
    return render(request, 'uform/user_personaldetails.html', {
        'personaldetails_form': personaldetails_form,
        'hobbies_form': hobbies_form,
    })

@login_required
def CareerFormView(request):
    if request.method == 'POST':
        career_form = CareerForm(request.POST, instance=request.user.userprofile)
        if career_form.is_valid():
            career_form.save()
            return HttpResponseRedirect(reverse('InterestFormView'))
    else:
        career_form = CareerForm(instance=request.user.userprofile)
    return render(request, 'uform/career.html', {
        'career_form': career_form,
    })

@login_required
def InterestFormView(request):
    if request.method == 'POST':
        interest_form = InterestForm(request.POST, instance=request.user.userprofile)
        if interest_form.is_valid():
            interest_form.save()
            return HttpResponseRedirect('/interact/get/random/book/')
    else:
        interest_form = InterestForm(instance=request.user.userprofile)
    return render(request, 'uform/interest.html', {
        'interest_form': interest_form,
    })
