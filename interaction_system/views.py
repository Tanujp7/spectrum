from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import BookRating
from vanilla import CreateView, DeleteView, ListView, UpdateView, DetailView, FormView

# Create your views here.

class BookRatingList(LoginRequiredMixin, ListView):
    model = BookRating
    paginate_by = 8