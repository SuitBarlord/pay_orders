from django.contrib import admin
from django.urls import path
from .views import UserLoginView, UserLogoutView

urlpatterns = [
    path('login/', UserLoginView.as_view()),
    path('logout/', UserLogoutView.as_view(), name='logout')
]