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


urlpatterns = [
    # Linking Django Admin's url file
    url(r'^admin/', admin.site.urls),

    # Linking interaction_system's url file
    url(r'^', include('people.urls')),

    # Linking interaction_system's url file
    url(r'^', include('items.urls')),

    # Linking interaction_system's url file
    url(r'^', include('interaction_system.urls')),

    # Linking google_books' url file
    url(r'^', include('google_books.urls')),

    # Linking uform's url file
    url(r'forms/^', include('uform.urls')),

    # Linking django-allauth's url file
    url(r'^accounts/', include('allauth.urls')),

]
