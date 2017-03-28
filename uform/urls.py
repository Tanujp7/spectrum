from django.conf.urls import url

# Class Based Views
# Function Based Views
from .views import UserProfileFormView

urlpatterns = [
    # Function Based Views
    url(r'^profile/$', UserProfileFormView, name='UserProfileFormView'),
]
