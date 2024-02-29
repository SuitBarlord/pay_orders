from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Reestr_oferts, Filials
from .forms import CreateOrderForm
from django.views.generic.edit import UpdateView
from .filters import ProductFilter




def main(request, *args, **kwargs):
    orders = Reestr_oferts.objects.all()
    sum = 0
    for order in orders:
        sum = sum + order.price
    
    context = {
        'orders': orders,
        'sum': sum
    }
    return render(request, 'orders/main.html', context=context)


def get_filials(request):
    filials = Filials.objects.all()
    context = {
        'filials': filials
    }
    return render(request, 'orders/main.html', context=context)

@login_required
def get_orders(request, pk):
    filter = ProductFilter(request.GET, queryset=Reestr_oferts.objects.filter(filial_id=pk))
    return render(request, 'orders/orders.html', {'filter': filter})
    # orders = Reestr_oferts.objects.filter(filial_id=pk)
    # filial = pk
    # context = {
    #     'orders': orders,
    #     'filial': filial
    # }
    # return render(request, 'orders/orders.html', context=context)
    


def get_order(request, id_order):
    order = Reestr_oferts.objects.get(pk=id_order)
    context = {
        'order': order
    }
    return render(request, 'orders/order.html', context=context)


def create_orders(request):
    if request.method == 'POST':
        order_form = CreateOrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()
            return redirect('/main/')
        else:
            return render(request, 'orders/create_order.html', {'form': order_form})
    else:
        order_form = CreateOrderForm()
        context = {
            'form': order_form
        }
        return render(request, 'orders/create_order.html', context=context)
    
# Редактирование записи модели
class EditOrder(UpdateView):
    model = Reestr_oferts
    form_class = CreateOrderForm
    template_name = 'orders/edit_order.html'
    success_url = '/main/'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['order'] = Reestr_oferts.objects.all()
        return context
        
        
