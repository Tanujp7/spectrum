from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import BookRating
from django.views import View
from vanilla import CreateView, DeleteView, ListView, UpdateView, DetailView, FormView

# Create your views here.

class BookRatingList(LoginRequiredMixin, ListView):
    model = BookRating
    paginate_by = 8

class UserProfile(LoginRequiredMixin, View):
    greeting = "Good Day!"
    template_name = 'interaction_system/user_profile.html'

    def get(self, request):
        return render(request, self.template_name)
