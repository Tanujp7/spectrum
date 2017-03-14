from django.conf.urls import url

from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy

from .views import BookRatingList, UserProfile

urlpatterns = [
    url(r'^book_rating/$', BookRatingList.as_view(), name='book_rating_list'),
    url(r'^about/$', UserProfile.as_view())
]
