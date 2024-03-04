from django.forms import ModelForm
from .models import Reestr_oferts, Exicuters
from django import forms

class CreateOrderForm(ModelForm):
    class Meta:
        model = Reestr_oferts
        fields = ('number_orders_vozm', 'fio', 'exicutor', 'filial', 'price', 'date_buhgt', 'comment')

        widgets = {
            'date_buhgt': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'date'
                      }),
        }


class CreateExicuterForm(ModelForm):
    class Meta:
        model = Exicuters
        fields = ('fio', 'filial')
        
        
class EditExicuterForm(ModelForm):
    class Meta:
        model = Exicuters
        fields = ('fio', 'filial')