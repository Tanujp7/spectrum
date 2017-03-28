from django.shortcuts import render, render_to_response
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import Permission, User
from django.contrib.auth.decorators import login_required

from .models import BookRating
from django.views import View
from vanilla import CreateView, DeleteView, ListView, UpdateView, DetailView, FormView

from allauth.account.views import LoginView

from .forms import UserProfileForm

def UserProfileFormView(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        location_form = LocationForm(request.POST, instance=request.user.location)
        qualification_form = QualificationForm(request.POST, instance=request.user.qualification)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and location_form.is_valid() and qualification_form.is_valid() and profile_form.is_valid():
            user_form.save()
            location_form.save()
            qualification_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully saved!'))
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        location_form = LocationForm(request.POST, instance=request.user.location)
        qualification_form = QualificationForm(request.POST, instance=request.user.qualification)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'interaction_system/user_profile.html', {
        'user_form': user_form,
        'location_form': location_form,
        'qualification_form': qualification_form,
        'profile_form': profile_form
    })

class AuthLoginView(LoginView):
    template_name = 'allauth/login.html'

class BookRatingList(LoginRequiredMixin, ListView):
    model = BookRating
    paginate_by = 8

class UserProfile(LoginRequiredMixin, View):
    greeting = "Good Day!"
    template_name = 'interaction_system/user_profile.html'

    def get(self, request):
        return render(request, self.template_name)
