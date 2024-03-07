from django.forms import ModelForm
from .models import Reestr_oferts, Exicuters, Filials
from django import forms

class CreateOrderForm(ModelForm):
    def __init__(self, *args, name_filial=None, exicutor=None, **kwargs):
        super().__init__(*args, **kwargs)
        if name_filial == None or exicutor == None:
            pass 
        else:
            self.fields['filial'].queryset = Filials.objects.filter(name=name_filial)
            self.fields['exicutor'].queryset = Exicuters.objects.filter(filial_id=exicutor)
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
        

class CreateExicuterFilialFilterForm(ModelForm):
    def __init__(self, *args, id=None, **kwargs):
        super().__init__(*args, **kwargs)
        if id == None:
            pass 
        else:
            self.fields['filial'].queryset = Filials.objects.filter(id=id)
    class Meta:
        model = Exicuters
        fields = ('fio', 'filial')
        
        
class EditExicuterForm(ModelForm):
    class Meta:
        model = Exicuters
        fields = ('fio', 'filial')
        
        
# from django import forms
# from myapp.models import MyModel

# class MyModelForm(forms.ModelForm):
#     def __init__(self, *args, route=None, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['related_records'].queryset = MyRelatedModel.objects.filter(route=route)
    
#     class Meta:
#         model = MyModel
#         fields = '__all__'
