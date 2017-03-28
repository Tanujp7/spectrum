from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View

class Search(View):
    template_name = 'google_books/search.html'

    def get(self, request):
        return render(request, self.template_name)
