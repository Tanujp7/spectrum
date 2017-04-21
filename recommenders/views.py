# Http Libraries
from django.shortcuts import render

# Auth
from django.contrib.auth.decorators import login_required

# Models
from interaction_system.models import BookRating

# Panda!
from recommenders.data import dataframe

## Functional Views start here..
@login_required
def bookrating_history(request):

    context = {}
    current_user = request.user

    df = dataframe(BookRating.objects.filter(user=current_user), fieldnames=['rating', 'book', 'created_at'], index='id')
    context['book_rating_history'], context['count'] = df, BookRating.objects.filter(user=current_user).count()

    return render(request, 'recommenders/bookrating_history.html', context)
