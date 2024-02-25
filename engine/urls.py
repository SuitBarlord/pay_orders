from django.contrib import admin
from django.urls import path
from .views import main, create_orders, get_order, EditOrder, get_filials, get_orders




urlpatterns = [
    path('main/', main),
    path('filials/', get_filials, name='get_filials'),
    path('filials/pay_orders/<int:pk>/', get_orders, name='get_orders'),
    path('filials/pay_orders/<int:id_filial>/order/<int:id_order>/', get_order, name='get_order'),
    path('pay_orders/create_order/', create_orders),
    path('filials/pay_orders/edit/<int:pk>/', EditOrder.as_view(), name='edit_order')
]