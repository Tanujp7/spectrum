# Models
from interaction_system.models import BookRating
from items.models import Book, BookProfile
from people.models import Career, Hobbies, Interest, PersonalDetails, UserProfile
from django.contrib.auth.models import User

# Django-pandas
from django_pandas.io import read_frame

def query_set(model):
    qs = model.objects.all()
    return qs

def dataframe(model,fieldnames=None,index=None):
    query_set = model.objects.all()
    if fieldnames:
        if index:
            data_frame = query_set.to_dataframe(fieldnames, index=index)
        else:
            data_frame = query_set.to_dataframe(fieldnames)
    else:
        if index:
            data_frame = query_set.to_dataframe(index=index)
        else:
            data_frame = read_frame(query_set)
    return data_frame
