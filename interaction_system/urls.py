from django.conf.urls import url

from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy

from .views import BookRatingList

urlpatterns = [
    url(r'^inventory/material/$', BookRatingList.as_view(), name='book_rating_list'),
]
