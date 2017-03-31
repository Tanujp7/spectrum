from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView

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

class AddBook(CreateView):
    template_name = 'google_books/add.html'

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

    def form_valid(self, form):
            return super(AddBook, self).form_valid(form)


@permission_required('items.add_book')
def add_book(request):

    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('book_search') )

    elif request.method == 'GET':
        form = BookForm()
        try:
            volume_id = request.GET.get('volume_id')
        except:
            volume_id = ''
        if (volume_id != '' and volume_id is not None):
            item = googlebooks.retrieve(volume_id)
        else:
            item = None
        return render(request, 'google_books/add.html', {'item' : item, 'form': form})

    return render(request, 'google_books/add.html', {'form': form})
