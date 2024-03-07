from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import JsonResponse

# Create your views here.
from .models import Reestr_oferts, Filials, Exicuters
from .forms import CreateOrderForm, CreateExicuterForm, EditExicuterForm, CreateExicuterFilialFilterForm
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

@login_required
def get_filials(request):
    if not request.user.has_perm('engine.view_reestr_oferts'):
        filials = Filials.objects.filter(name=request.user.filial)
    else:
        filials = Filials.objects.all()
    context = {
        'filials': filials
    }
    return render(request, 'orders/filials.html', context=context)


@login_required
def get_orders(request, pk):
    if not request.user.has_perm('engine.view_reestr_oferts'):
        # Проверка на придлежность пользователя к филиалу, который передается в параметре маршрута
        queryset = Reestr_oferts.objects.filter(filial_id=pk)
        exicuters_filial = Exicuters.objects.filter(filial_id=pk)
        # Проверка на пустой QuerySet
        if not queryset:
            form = CreateExicuterFilialFilterForm(id=pk)
            # Инициализация выбора поля со связанной моделью по умолчанию
            form.initial['filial'] = pk
            exicuters_filial = Exicuters.objects.filter(filial_id=pk)
            filter = ProductFilter(request.GET, queryset=Reestr_oferts.objects.filter(filial_id=pk), id=pk)
            return render(request, 'orders/orders.html', {'filter': filter, 'exicuters_filial': exicuters_filial, 'form': form})
        else:
            filial = str(queryset[0].filial)
            user_filial = str(request.user.filial)
            if filial == user_filial:
                form = CreateExicuterFilialFilterForm(id=pk)
                # Инициализация выбора поля со связанной моделью по умолчанию
                form.initial['filial'] = pk
                filter = ProductFilter(request.GET, queryset=Reestr_oferts.objects.filter(filial_id=pk), id=pk)
                return render(request, 'orders/orders.html', {'filter': filter, 'exicuters_filial': exicuters_filial, 'form': form})
            else: 
                # Принудительное исключение 
                raise PermissionError
    else:
        
        form = CreateExicuterFilialFilterForm(id=None)
        # Инициализация выбора поля со связанной моделью по умолчанию
        form.initial['filial'] = pk
        # if request.method == "POST":
        #     form = CreateExicuterForm(request.POST)
        #     if form.is_valid():
                
        #         form.save()
        #         # return JsonResponse({'fio':fio, 'filial':filial}, status=200)
        #     else:
        #         errors = form.errors.as_json()
        #         return JsonResponse({'errors':errors}, status=400)

        exicuters_filial = Exicuters.objects.filter(filial_id=pk)
        filter = ProductFilter(request.GET, queryset=Reestr_oferts.objects.filter(filial_id=pk), id=pk)
        return render(request, 'orders/orders.html', {'filter': filter, 'exicuters_filial': exicuters_filial, 'form': form})
    
    
def create_exicuter(request):
    if request.method == 'POST':
        if not request.user.has_perm('engine.add_exicuters'):
            raise PermissionError
        else:
            exicuter_form = CreateExicuterForm(request.POST)
            if exicuter_form.is_valid():
                exicuter_form.save()
                return redirect('/paid_departure/filials/')
            else:
                pass
                
    # else:
    #     exicuter_form = CreateExicuterForm()
    #     context = {
    #         'form': exicuter_form
    #     }
    #     return render(request, 'orders/create_exicuter.html', context=context)
    

@login_required
def get_order(request, id_order):
    if not request.user.has_perm('engine.view_reestr_oferts'):
        queryset = Reestr_oferts.objects.get(pk=id_order)
        filial = str(queryset.filial)
        user_filial = str(request.user.filial)
        if filial == user_filial:
            order = Reestr_oferts.objects.get(pk=id_order)
        else:
            raise PermissionError
    else:
        order = Reestr_oferts.objects.get(pk=id_order)
    context = {
        'order': order
    }
    return render(request, 'orders/order.html', context=context)


@login_required
def create_orders(request):
    if request.method == 'POST':
        if not request.user.has_perm('engine.add_reestr_oferts'):
            raise PermissionError
        else:
            order_form = CreateOrderForm(request.POST)
            if order_form.is_valid():
                order_form.save()
                return redirect('/paid_departure/filials/')
            else:
                return render(request, 'orders/create_order.html', {'form': order_form})
    else:
        if not request.user.has_perm('engine.view_reestr_oferts'):
            print(request.user.filial)
            id_filial = Filials.objects.filter(name=request.user.filial)
            print(id_filial[0].id)
            order_form = CreateOrderForm(name_filial=request.user.filial, exicutor=id_filial[0].id)
            context = {
                'form': order_form
            }
            return render(request, 'orders/create_order.html', context=context)
        else:
            order_form = CreateOrderForm()
            context = {
                'form': order_form
            }
            return render(request, 'orders/create_order.html', context=context)
    
# Редактирование записи модели
class EditOrder(PermissionRequiredMixin, UpdateView):
    permission_required = 'engine.change_reestr_oferts'
    model = Reestr_oferts
    form_class = CreateOrderForm
    template_name = 'orders/edit_order.html'
    success_url = '/paid_departure/filials/'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['order'] = Reestr_oferts.objects.all()
        return context
        

class EditExicutor(PermissionRequiredMixin, UpdateView):
    permission_required = 'engine.change_reestr_oferts'
    model = Exicuters
    form_class = EditExicuterForm
    template_name = 'orders/edit_exicuter.html'
    success_url = '/paid_departure/filials/'

    def get_context_data(self, *args, **kwargs): 
        context = super().get_context_data(*args, **kwargs)
        context['exicuter'] = Exicuters.objects.all()
        return context
    

import PyPDF2
def pdf(request):
    import PyPDF2

    # Открываем исходный файл PDF
    from PyPDF2 import PdfFileReader, PdfFileWriter
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    # Открыть исходный файл PDF
    with open('example.pdf', 'rb') as file:
        pdf = PdfFileReader(file)

        # Создать новый файл PDF для записи
        output = PdfFileWriter()

        # Получить первую страницу документа
        page = pdf.getPage(0)

        # Создать новую страницу с теми же размерами, что и исходная
        c = canvas.Canvas('вставленный_файл.pdf', pagesize=letter)
        pdfmetrics.registerFont(TTFont('CustomFont', 'helvetica.ttf'))
        # Установить нужный шрифт и размер
        c.setFont('CustomFont', 14)

        # Вставить текст на новой странице
        c.drawString(200, 400, 'Новая строка')

        # Завершить рисование на новой странице
        c.save()

        # Прочитать вставленный файл PDF
        with open('вставленный_файл.pdf', 'rb') as inserted:
            inserted_pdf = PdfFileReader(inserted)

            # Получить вставленную страницу
            inserted_page = inserted_pdf.getPage(0)

            # Скопировать содержимое исходной страницы на новую
            inserted_page.mergeTranslatedPage(page, 0, 0, expand=False)

            # Добавить страницу в новый документ
            output.addPage(inserted_page)

            # Добавить оставшиеся страницы исходного файла
            for i in range(1, pdf.getNumPages()):
                output.addPage(pdf.getPage(i))

            # Сохранить новый файл
            with open('измененный_файл.pdf', 'wb') as output_file:
                output.write(output_file)








from django.http import HttpResponse
from django.shortcuts import render
from docx import Document
from docxtpl import DocxTemplate
def preview_template(request):
        doc = DocxTemplate("example.docx")
        context = { 'director' : "И.И.Иванов"}
        doc.render(context)
        doc.save("final.docx")




