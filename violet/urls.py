"""violet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic.base import TemplateView
admin.autodiscover()

urlpatterns = [
    # Linking Django Admin's url file
    url(r'^admin/', admin.site.urls),

    # Linking django-allauth's url file
    url(r'^accounts/', include('allauth.urls')),

    # Linking interaction_system's url file
    url(r'^', include('interaction_system.urls')),

    # django-allauth
    url(r'^$', TemplateView.as_view(template_name='allauth/index.html')),
    url(r'^accounts/profile/$', TemplateView.as_view(template_name='allauth/profile.html')),
    url(r'^accounts/email/$', TemplateView.as_view(template_name='allauth/email.html')),
    url(r'^accounts/login/$', TemplateView.as_view(template_name='allauth/login.html')),
]
