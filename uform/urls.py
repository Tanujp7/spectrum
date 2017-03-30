from django.conf.urls import url

# Class Based Views
# Function Based Views
from .views import UserProfileFormView, PersonalDetailsFormView, CareerFormView

urlpatterns = [
    # Function Based Views
    url(r'^personal/$', PersonalDetailsFormView, name='PersonalDetailsFormView'),
    url(r'^profile/$', UserProfileFormView, name='UserProfileFormView'),
    url(r'^career/$', CareerFormView, name='CareerFormView'),
]
