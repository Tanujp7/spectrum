from django.shortcuts import render

from allauth.account.views import LoginView

class AuthLoginView(LoginView):
    template_name = 'allauth/login.html'
