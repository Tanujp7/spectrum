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

    def get(self, request):
        return HttpResponse(self.greeting)
