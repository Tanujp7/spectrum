from django.conf.urls import url
from .views import rate_the_book, random_book

urlpatterns = [
    url(r'^get/random/book/$', random_book, name='rate_random_book'),
    url(r'^book/rate/(?P<volume>([A-Za-z0-9\-\_]+))/$', rate_the_book, name='rate_book'),
]
