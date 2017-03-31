from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from items.models import Book, BookProfile

from .forms import BookRatingForm, RatingLogForm


@login_required
def random_book(request):
    book = None
    while True:
        try:
            book = Book.random.all()[0]
            volume_id = book.volume_id
            return redirect(reverse('rate_book',kwargs={'volume':volume_id}))
        except:
            pass

@login_required
def rate_the_book(request, volume=""):

    # Redirect in case /book/rate/random/ doesn't pick 'random_book()'
    #if volume == "random":
    #    return HttpResponseRedirect(reverse('book_search'))

    # When book is rated!
    if request.method == 'POST':
        book_rating_form = BookRatingForm(request.POST)

        book_obj = Book.objects.get(volume_id=volume)
        user_obj = request.user

        if book_rating_form.is_valid():
            brf = book_rating_form.save(commit=False)
            brf.book = book_obj
            brf.user = user_obj
            brf.save()
            book_rating_form.save_m2m()

        rating = request.POST.get('rating')

        rating_log_form = RatingLogForm(request.POST)

        if rating_log_form.is_valid():
            rlf = rating_log_form.save(commit=False)
            rlf.book_rating = BookRating.objects.order_by('book', 'user').distinct('book', 'user')[:1].get()
            rlf.rating = rating
            rlf.save()
            rating_log_form.save_m2m()

            # Success and Now NEXT book
            return HttpResponseRedirect(reverse('rate_random_book'))

        # Form(s) were not valid. Something bad happend. Go home!
        return HttpResponseRedirect(reverse('home'))

    # Load form on the page
    book_rating_form = BookRatingForm()
    rating_log_form = RatingLogForm()

    # Let's show the page w/ forms and book item.
    context = { }

    # Get Book & BookProfile Object w/ matching volume_id
    if (volume != '' and volume is not None):
        try:
            book = Book.objects.get(volume_id=volume)
            book_profile = BookProfile.objects.get(book=book)
            context = { 'book' : book,
                        'book_profile' : book_profile,
                        'book_rating_form': book_rating_form,
                        'rating_log_form': rating_log_form
                        }
        except:
            return HttpResponseRedirect(reverse('home'))


    return render(request, 'interaction_system/rate_book.html', context)
