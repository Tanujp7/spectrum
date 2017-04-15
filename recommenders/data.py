from interaction_system.models import BookRating
from django_pandas.io import read_frame

def get_dataframe(model):
    qs = model.objects.all()
    df = read_frame(qs)
    return df
