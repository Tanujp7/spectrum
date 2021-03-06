from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.db import IntegrityError

from items.models import Book, BookProfile
from .models import BookRating

from .forms import BookRatingForm

import random

@login_required
def random_book(request):
    books = Book.objects.all()

    current_user = request.user
    bookratings_by_currentuser = BookRating.objects.filter(user=current_user)
    booklist_by_user = []

    for r in bookratings_by_currentuser.values('book'):
        booklist_by_user.append(r['book'])

    books_not_rated_by_user = books.exclude(id__in=booklist_by_user)
    random_book = random.choice(books_not_rated_by_user)
    volume_id = random_book.volume_id

    return redirect(reverse('rate_book',kwargs={'volume':volume_id}))

@login_required
def rate_the_book(request, volume=""):

    def show_book(messages=None):
        book_rating_form = BookRatingForm()
        context = {}

        current_user = request.user
        bookratings_count_by_currentuser = BookRating.objects.filter(user=current_user).count()
        if bookratings_count_by_currentuser is None: bookratings_count_by_currentuser = 0
        # Get Book & BookProfile Object w/ matching volume_id
        if (volume != '' and volume is not None):
            try:
                book = Book.objects.get(volume_id=volume)
                book_profile = BookProfile.objects.get(book=book)

                # Let's show the page w/ forms and book item.
                context = { 'book' : book,
                            'book_profile' : book_profile,
                            'book_rating_form': book_rating_form,
                            'messages' : messages,
                            'count' : bookratings_count_by_currentuser
                            }
            except:
                return HttpResponseRedirect(reverse('home'))

        return render(request, 'interaction_system/rate_book.html', context)

    # When book is rated!
    if request.method == 'POST':
        book_rating_form = BookRatingForm(request.POST)

        book_obj = Book.objects.get(volume_id=volume)
        user_obj = request.user

        if book_rating_form.is_valid():
            brf = book_rating_form.save(commit=False)
            brf.book = book_obj
            brf.user = user_obj
            try:
                brf.save()
            except IntegrityError as e:
                return show_book(messages=["You've already rated this book.", "Click on 'Rate Books' to go to a random Book."])
            book_rating_form.save_m2m()
            # Success and Now NEXT book
            return HttpResponseRedirect(reverse('rate_random_book'))
        else:
            return HttpResponse('An error occured? / book_rating_form isnt valid')

    return show_book()
