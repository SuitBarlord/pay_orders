from django.shortcuts import render, redirect

# Create your views here.
from .models import Reestr_oferts
from .forms import CreateOrderForm



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
        
