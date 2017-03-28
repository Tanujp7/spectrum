from django.conf.urls import url, include

from django.views.generic import RedirectView
from django.views.generic.base import TemplateView
from django.core.urlresolvers import reverse_lazy

from .views import BookRatingList, UserProfile, AuthLoginView


urlpatterns = [
    url(r'^book_rating/$', BookRatingList.as_view(), name='book_rating_list'),
    url(r'^user_profile/$', UserProfile.as_view(), name='user_profile'),

    # django-allauth
    url(r'^$', TemplateView.as_view(template_name='allauth/index.html')),
    url(r'^accounts/profile/$', TemplateView.as_view(template_name='allauth/profile.html')),
    url(r'^accounts/email/$', TemplateView.as_view(template_name='allauth/email.html')),
    url(r'^accounts/login/$', AuthLoginView.as_view()),

    url(r'^accounts/location/$', views.location_form, name='location_form'),
]
