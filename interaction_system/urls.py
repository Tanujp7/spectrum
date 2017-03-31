from django.conf.urls import url
from .views import rate_the_book

urlpatterns = [
    url(r'^book/rate/random/$', rate_the_book, name='rate_random_book'),
    url(r'^book/rate/(?P<volume>\w+)/$', rate_the_book, name='rate_book'),
]
