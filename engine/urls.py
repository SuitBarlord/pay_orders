from django.contrib import admin
from django.urls import path
from .views import main, create_orders, get_order, EditOrder, get_filials, get_orders, EditExicutor, create_exicuter, preview_template, create_document, EditContractData, download_document




urlpatterns = [
    path('main/', main),
    path('filials/', get_filials, name='get_filials'),
    path('filials/orders/<int:pk>/', get_orders, name='get_orders'),
    path('filials/orders/order/<int:id_order>/', get_order, name='get_order'),
    path('create_order/', create_orders),
    path('filials/orders/edit/<int:pk>/', EditOrder.as_view(), name='edit_order'),
    path('filials/edit_exicuter/<int:pk>/', EditExicutor.as_view(), name='edit_exicutor'),
    path('filials/create_exicuter/', create_exicuter, name='create_exicuter'),
    path('filials/orders/order/create_document/<int:id_order>/', create_document, name='create_document'),
    path('filials/orders/order/edit_document/<int:pk>/', EditContractData.as_view(), name='edit_document'),
    path('filials/orders/order/download/<int:id_document>/', download_document, name='download_document'),
    # path('pdf/', pdf),
    path('preview_docx/<int:id_document>/', preview_template, name='preview_docx'),
]