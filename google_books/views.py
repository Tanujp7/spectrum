from django.shortcuts import render
from django.views import View

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










# Decorators
from django.contrib.auth.decorators import login_required

# Forms
from .forms import AddBookForm, AddBookProfileForm

from items.models import Book, BookProfile

def AddBookFormView(request):
    if request.method == 'POST':
        book_form = AddBookForm(request.POST, instance=request.book)
        profile_form = AddBookProfileForm(request.POST, instance=request.book.bookprofile)
        if book_form.is_valid() and profile_form.is_valid():
            book_form.save()
            profile_form.save()
    else:
        book_form = AddBookForm(instance=request.book)
        profile_form = AddBookProfileForm(instance=request.book.bookprofile)
    return render(request, 'uform/test.html', {
        'book_form': book_form,
        'bookprofile_form': profile_form
    })
