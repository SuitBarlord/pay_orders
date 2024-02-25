from django.forms import ModelForm
from .models import Reestr_oferts

class CreateOrderForm(ModelForm):
    class Meta:
        model = Reestr_oferts
        fields = ('number_orders_vozm', 'fio', 'exicutor', 'filial', 'price', 'date_buhgt', 'comment')