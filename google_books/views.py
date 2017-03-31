from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from items.models import Book, BookProfile
from .forms import BookForm

from google_books import googlebooks

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

class AddBook(View):
    template_name = 'google_books/add.html'
    success_url = '/'
    form_class = None

    def get(self, request):
        try:
            volume_id = request.GET.get('volume_id')
        except:
            volume_id = ''
        if (volume_id != '' and volume_id is not None):
            item = googlebooks.retrieve(volume_id)
        else:
            item = None
        return render(request, self.template_name, {'item' : item})

    def post(request):
        book_form = BookForm(request.POST)

        if book_form.is_valid():
            book_form.save()
            return redirect('book_search')
        else:
            return render(request, 'google_books/add.html', {
                'book_form': book_form
            })
