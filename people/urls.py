from django.conf.urls import url

from django.views.generic.base import TemplateView

# Class Based Views
from .views import AuthLoginView
# Function Based Views

urlpatterns = [
    # django-allauth
    url(r'^$', TemplateView.as_view(template_name='allauth/index.html')),
    url(r'^accounts/profile/$', TemplateView.as_view(template_name='allauth/profile.html')),
    url(r'^accounts/email/$', TemplateView.as_view(template_name='allauth/email.html')),
    url(r'^accounts/login/$', AuthLoginView.as_view()),
]
