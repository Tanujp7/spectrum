from django.shortcuts import render

from allauth.account.views import LoginView, LogoutView, SignupView

class AuthLoginView(LoginView):
    template_name = 'allauth/login.html'

class AuthLogoutView(LogoutView):
    template_name = 'allauth/logout.html'

class AuthSignupView(SignupView):
    template_name = 'allauth/signup.html'
