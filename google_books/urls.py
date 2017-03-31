from django.conf.urls import url, include
from django.contrib.auth.decorators import permission_required

from .views import Search, add_book


urlpatterns = [
    url(r'^search/$', permission_required('items.add_book', raise_exception=True)(Search.as_view()), name='book_search'),
    url(r'^add/$', add_book, name='book_add'),
]
