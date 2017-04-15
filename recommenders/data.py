from interaction_system.models import BookRating
from django_pandas.io import read_frame

def get_data(model):
    qs = model.objects.all()
    return qs
