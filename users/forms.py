from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'first_name', 'last_name', 'groups', 'user_permissions', 'filial', 'root_dir_user', 'is_personal')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'first_name', 'last_name', 'groups', 'user_permissions', 'filial', 'root_dir_user', 'is_personal')