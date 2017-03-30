from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required, permission_required

from google_books import googlebooks

@method_decorator(login_required, name='dispatch')
@method_decorator(permission_required, name='dispatch')
class Search(View):
    template_name = 'google_books/search.html'

    def get(self, request):
        try:
            query = request.GET.get('q')
        except:
            query = ''
        if (query != '' and query is not None):
            results = googlebooks.search(query.replace(" ", "+"))
        else:
            results = None
        return render(request, self.template_name, {'query' : query, 'results' : results})
