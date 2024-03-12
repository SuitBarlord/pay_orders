from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import JsonResponse

# Create your views here.
from .models import Reestr_oferts, Filials, Exicuters, Contract_Data
from .forms import CreateOrderForm, CreateExicuterForm, EditExicuterForm, CreateExicuterFilialFilterForm, CreateContractData, EditContractData
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
        # reestr_ofert = Reestr_oferts.objects.get(pk=2)
        filter = ProductFilter(request.GET, queryset=Reestr_oferts.objects.filter(filial_id=pk), id=pk)
        # document = reestr_ofert.contract_data
        # print(document)
        filial = Filials.objects.get(pk=pk)
        import os

        folder_path = f"dox/{filial.directory}"
        orders = Reestr_oferts.objects.filter(filial_id=pk)
        files = tuple(orders.values_list('number_orders_vozm', flat=True))
        files_orders = [element + '.docx' for element in files]
        print(files_orders)
        # file_names = ["имя_файла1", "имя_файла2", "имя_файла3"]
        ready_files = []

        if os.path.exists(folder_path):
            files = os.listdir(folder_path)
            for file in files_orders:
                if file in files:
                    ready_files.append(file)
                else:
                    ready_files.append(None)
        print(ready_files)
            # existing_files = [file for file in files if file in files]
            # missing_files = [file for file in files if file not in files]
            # print(existing_files)
            # print(missing_files)
        #     if missing_files:
        #         print("Следующие файлы отсутствуют в папке:")
        #         for file in missing_files:
        #             print(file)
        #     else:
        #         print("Все файлы присутствуют в папке.")
        # else:
        #     print("Папка не существует.")

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
            import os
            filial = order.filial.directory
            folder_path = f"dox/{filial}"
            orders = Reestr_oferts.objects.filter(pk=id_order)
            files = tuple(orders.values_list('number_orders_vozm', flat=True))
            files_orders = [element + '.docx' for element in files]
            print(files_orders)
            # file_names = ["имя_файла1", "имя_файла2", "имя_файла3"]
            ready_files = []

            if os.path.exists(folder_path):
                files = os.listdir(folder_path)
                for file in files_orders:
                    if file in files:
                        ready_files.append(file)
            print(ready_files)
        else:
            raise PermissionError
    else:
        order = Reestr_oferts.objects.get(pk=id_order)
        # print(order.contract_data.reestr_oferts_id)

        filial = order.filial.directory
        import os

        folder_path = f"dox/{filial}"
        orders = Reestr_oferts.objects.filter(pk=id_order)
        files = tuple(orders.values_list('number_orders_vozm', flat=True))
        files_orders = [element + '.docx' for element in files]
        print(files_orders)
        # file_names = ["имя_файла1", "имя_файла2", "имя_файла3"]
        ready_files = []

        if os.path.exists(folder_path):
            files = os.listdir(folder_path)
            for file in files_orders:
                if file in files:
                    ready_files.append(file)
        print(ready_files)


    context = {
        'order': order,
        'ready_files': ready_files
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
            id_filial = Filials.objects.filter(name=request.user.filial)
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
    

@login_required
def create_document(request, id_order):
    if request.method == 'POST':
        if not request.user.has_perm('engine.add_reestr_oferts'):
            raise PermissionError
        else:
            document_form = CreateContractData(request.POST)
            ready = Contract_Data.objects.filter(reestr_oferts=id_order)
            print(ready)
            if document_form.is_valid():
                document_form.save()
                return redirect('/paid_departure/filials/')
    else:
        ready = Contract_Data.objects.filter(reestr_oferts=id_order)
        if not ready:
            document_form = CreateContractData(reestr_oferts=id_order)
            context = {
                'form': document_form
            }
            return render(request, 'orders/create_document.html', context=context)
        else: 
            return redirect('/main/')
        

class EditContractData(PermissionRequiredMixin, UpdateView):
    permission_required = 'engine.change_contract_data'
    model = Contract_Data
    form_class = EditContractData
    template_name = 'orders/edit_contract.html'
    success_url = '/paid_departure/filials/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['contract_data'] = Contract_Data.objects.all()
        return context
        

    

# import PyPDF2
# def pdf(request):
#     import PyPDF2

#     # Открываем исходный файл PDF
#     from PyPDF2 import PdfFileReader, PdfFileWriter
#     from reportlab.lib.pagesizes import letter
#     from reportlab.pdfgen import canvas
#     from reportlab.pdfbase import pdfmetrics
#     from reportlab.pdfbase.ttfonts import TTFont
#     # Открыть исходный файл PDF
#     with open('example.pdf', 'rb') as file:
#         pdf = PdfFileReader(file)

#         # Создать новый файл PDF для записи
#         output = PdfFileWriter()

#         # Получить первую страницу документа
#         page = pdf.getPage(0)

#         # Создать новую страницу с теми же размерами, что и исходная
#         c = canvas.Canvas('вставленный_файл.pdf', pagesize=letter)
#         pdfmetrics.registerFont(TTFont('CustomFont', 'helvetica.ttf'))
#         # Установить нужный шрифт и размер
#         c.setFont('CustomFont', 14)

#         # Вставить текст на новой странице
#         c.drawString(200, 400, 'Новая строка')

#         # Завершить рисование на новой странице
#         c.save()

#         # Прочитать вставленный файл PDF
#         with open('вставленный_файл.pdf', 'rb') as inserted:
#             inserted_pdf = PdfFileReader(inserted)

#             # Получить вставленную страницу
#             inserted_page = inserted_pdf.getPage(0)

#             # Скопировать содержимое исходной страницы на новую
#             inserted_page.mergeTranslatedPage(page, 0, 0, expand=False)

#             # Добавить страницу в новый документ
#             output.addPage(inserted_page)

#             # Добавить оставшиеся страницы исходного файла
#             for i in range(1, pdf.getNumPages()):
#                 output.addPage(pdf.getPage(i))

#             # Сохранить новый файл
#             with open('измененный_файл.pdf', 'wb') as output_file:
#                 output.write(output_file)








from django.http import HttpResponse
from django.shortcuts import render
from docx import Document
from docxtpl import DocxTemplate
@login_required
def preview_template(request, id_document):
    order = Reestr_oferts.objects.get(pk=id_document)
    document_data = Contract_Data.objects.get(reestr_oferts_id=id_document)
    exicutor = Exicuters.objects.get(pk=order.exicutor_id)
    filial = Filials.objects.get(pk=order.filial_id)
    print(document_data)

    name_parts = exicutor.fio.split()

    fio = name_parts[0]
    initials = name_parts[1][0] + '.' + name_parts[2][0] + '.'
    exicutor_short = fio + ' ' + initials

    name_parts_order = order.fio.split()
    
    fio_order = name_parts_order[0]
    initials_order = name_parts_order[1][0] + '.' + name_parts_order[2][0] + '.'
    fio_short = fio_order + ' ' + initials_order


    doc = DocxTemplate("example.docx")
    context = { 'number' : document_data.reestr_oferts, 
               'fio': order.fio, 
               'fio_short': fio_short,
               'identification_document': document_data.identification_document, 
               'passport_series': document_data.passport_series, 
               'number_passport': document_data.number_passport, 
               'document_issue_date': document_data.document_issue_date,
               'location': document_data.location,
               'price': order.price,
               'adress': document_data.adress,
               'exicutor_position': exicutor.position_filial,
               'exicutor': exicutor.fio,
               'exicutor_short': exicutor_short,
               'document_issuing_authority': document_data.document_issuing_authority
               }
    doc.render(context)
    doc.save(f"dox/{filial.directory}/{order.number_orders_vozm}.docx")
    
    # return JsonResponse({'status': 200})
    return redirect(f'/paid_departure/filials/orders/order/{id_document}/')

    
    # doc = DocxTemplate("example.docx")
    # context = { 'number' : "И.И.Иванов"}
    # doc.render(context)
    # doc.save("final.docx")




