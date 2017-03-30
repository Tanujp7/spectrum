from django.conf.urls import url, include

from .views import Search


urlpatterns = [
    url(r'^search/$', Search.as_view(), name='book_search'),
]
