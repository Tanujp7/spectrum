from django.conf.urls import url, include
from django.contrib.auth.decorators import permission_required

from .views import Search


urlpatterns = [
    url(r'^search/$', permission_required('items.add_book')(Search.as_view()), name='book_search'),
]
