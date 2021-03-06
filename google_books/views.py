from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.views import View
from django.views.generic.edit import CreateView

from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


from items.models import Book, BookProfile
from .forms import BookForm, BookProfileForm

from google_books import googlebooks

from recommenders import language_api as nl

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

@permission_required('items.add_book')
def add_book(request):

    if request.method == 'POST':

        # Saving Book object
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()

        # Calling just-saved Book object
        volume_id = request.POST.get('volume_id')
        book_obj = Book.objects.get(volume_id=volume_id)

        # Modifying & Saving BookProfile object
        book_profile_form = BookProfileForm(request.POST)
        if book_form.is_valid() and book_profile_form.is_valid():
            instance = book_profile_form.save(commit=False)
            instance.book = book_obj
            instance.save()
            nl.api_call(instance)       # For G-NLP & MC-IPTC
            book_profile_form.save_m2m()

            return HttpResponseRedirect(reverse('book_search'))

        return render(request, 'google_books/add.html', {'book_form': book_form, 'book_profile_form': book_profile_form})

    else:

        book_form = BookForm()
        book_profile_form = BookProfileForm()

        try:
            volume_id = request.GET.get('volume_id')
        except:
            volume_id = ''

        if (volume_id != '' and volume_id is not None):
            item = googlebooks.retrieve(volume_id)
        else:
            item = None

        return render(request, 'google_books/add.html', {'item' : item, 'book_form': book_form, 'book_profile_form': book_profile_form})

    return render(request, 'google_books/add.html', {'book_form': book_form, 'book_profile_form': book_profile_form})
