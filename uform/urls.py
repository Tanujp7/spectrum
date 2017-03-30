from django.conf.urls import url

# Class Based Views
# Function Based Views
from .views import UserProfileFormView, PersonalDetailsFormView

urlpatterns = [
    # Function Based Views
    url(r'^personal/$', PersonalDetailsFormView, name='PersonalDetailsFormView'),
    url(r'^profile/$', UserProfileFormView, name='UserProfileFormView'),
]
