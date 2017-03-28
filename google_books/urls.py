from django.conf.urls import url, include

from .views import Search


urlpatterns = [
    url(r'^book/add/search/$', Search.as_view(), name='book_search'),
]
