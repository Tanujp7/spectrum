from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import BookRating
from django.views import View
from vanilla import CreateView, DeleteView, ListView, UpdateView, DetailView, FormView

from allauth.account.views import LoginView

from .forms import UserProfileForm

def UserProfileFormView(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
    else:
        form = UserProfileForm()
    return render_to_response('interaction_system/user_profile.html', {'form': form}, context)

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
