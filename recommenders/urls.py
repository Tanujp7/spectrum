from django.conf.urls import url
from .views import bookrating_history

urlpatterns = [
    url(r'^rating/history/$', bookrating_history, name='bookrating_history'),
]
