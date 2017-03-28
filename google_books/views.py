from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View

class Search(View):
    template_name = 'google_books/search.html'

    def get(self, request):
        results = "Blank"
        try:
            query = request.GET.get('q')
        except:
            query = ''
        if (query != ''):
            results = "Nothing '" + query + "'"
        else:
            results = "Something '" + query + "'"
        return render(request, self.template_name, {'r': results})
