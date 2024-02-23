from django.contrib import admin
from django.urls import path
from .views import main, create_orders, get_order, EditOrder




urlpatterns = [
    path('main/', main),
    path('pay_orders/order/<int:pk>/', get_order, name='get_order'),
    path('pay_orders/create_order/', create_orders),
    path('pay_orders/edit/<int:pk>/', EditOrder.as_view())
]