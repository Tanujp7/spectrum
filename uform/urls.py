from django.conf.urls import url

# Class Based Views
# Function Based Views
from .views import UserProfileFormView, PersonalDetailsFormView, CareerFormView, InterestFormView

urlpatterns = [
    # Function Based Views
    url(r'^profile/$', UserProfileFormView, name='UserProfileFormView'),
    url(r'^personal/$', PersonalDetailsFormView, name='PersonalDetailsFormView'),
    url(r'^career/$', CareerFormView, name='CareerFormView'),
    url(r'^interest/$', InterestFormView, name='InterestFormView'),
]
