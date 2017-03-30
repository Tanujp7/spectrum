from django.conf.urls import url

from django.views.generic.base import TemplateView

# Class Based Views
from .views import AuthLoginView, AuthLogoutView, AuthSignupView
# Function Based Views

urlpatterns = [
    # django-allauth
    url(r'^profile/$', TemplateView.as_view(template_name='allauth/profile.html')),
    url(r'^email/$', TemplateView.as_view(template_name='allauth/email.html')),
    url(r'^login/$', AuthLoginView.as_view()),
    url(r'^logout/$', AuthLogoutView.as_view()),
    url(r'^signup/$', AuthSignupView.as_view()),
]
