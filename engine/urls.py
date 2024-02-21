from django.contrib import admin
from django.urls import path
from .views import main, create_orders




urlpatterns = [
    path('main/', main),
    path('create_orders/', create_orders)
]