from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm
# Create your views here.


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    # authentication_form = LoginForm
    # form_class = LoginForm
    
class UserLogoutView(LogoutView):
    # template_name = 'users/logout.html'
    # pass
    redirect_field_name = '/paid_departure/filials/'