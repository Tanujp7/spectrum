from django.shortcuts import render

from allauth.account.views import LoginView, LogoutView

class AuthLoginView(LoginView):
    template_name = 'allauth/login.html'

class AuthLogoutView(LogoutView):
    template_name = 'allauth/logout.html'
