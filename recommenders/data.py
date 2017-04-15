# Models
from interaction_system.models import BookRating
from items.models import Book, BookProfile
from people.models import Career, Hobbies, Interest, PersonalDetails, UserProfile
from django.contrib.auth.models import User

# Django-pandas
from django_pandas.io import read_frame

def dataframe(model):
    query_string = model.objects.all()
    data_frame = read_frame(query_string)
    return data_frame
