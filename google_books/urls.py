from django.conf.urls import url, include

from .views import Search


urlpatterns = [
    url(r'^google_books/search/$', Search.as_view(), name='book_search'),
]
