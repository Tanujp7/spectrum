# Django-pandas
from django_pandas.io import read_frame

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
