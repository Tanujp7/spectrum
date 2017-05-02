# Django-pandas
from django_pandas.io import read_frame

from recommenders import models as md

import numpy as np

def dataframe(query_set,fieldnames=None,index=None):
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

def get_data():
    # k2d = KeyToDocLink
    k2d_qs = mo.KeyToDocLink.objects.all()
    k2d = dataframe(k2d_qs)
    print(k2d)

if __name__ == '__main__':
    pass
