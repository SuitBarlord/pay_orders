from celery import shared_task
from django.core.mail import send_mail
from .models import Reestr_oferts
import time
from django.http import HttpResponse
from django.shortcuts import render
from docx import Document
from docxtpl import DocxTemplate
import pymorphy3
from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.
from .models import Reestr_oferts, Filials, Exicuters, Contract_Data
from .forms import CreateOrderForm, CreateExicuterForm, EditExicuterForm, CreateExicuterFilialFilterForm, CreateContractData, EditContractData
from django.views.generic.edit import UpdateView
from .filters import ProductFilter
import time 

@shared_task
def order_created(id_document):
    import time 
    # procces = 'celery create'
    time.sleep(20)
    # print('Celery')
    
    # return procces
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




    def change_case(fio, case):
        morph = pymorphy3.MorphAnalyzer()
        parsed = morph.parse(fio)[0]
        # Морфологический анализ фамилии
        parsed_name = morph.parse(fio)

        # Поиск нужной формы
        for form in parsed_name:
            if 'Surn' in form.tag and exicutor.gender in form.tag:  # Проверка, что это фамилия в женском роде
                print('Родительный падеж:', form.inflect({'gent'}).word)
                return form.inflect({'gent'}).word

        # return parsed.inflect({case}).word

    last_name = fio
    case = "gent"

    changed_fio = change_case(last_name, case).capitalize()

    print(changed_fio)

    from datetime import datetime

    # date_object = datetime.strptime(str(order.date_akt), '%Y-%m-%d')
    # formatted_date = date_object.strftime('%d %B %Y')
    # print(formatted_date)  # Output: 20 March 2024

    # from datetime import datetime
    # import calendar
    
    # date_object = datetime.strptime(str(order.date_akt), '%Y-%m-%d').date()

    # month_number = date_object.month
    # month_name = calendar.month_name[month_number]

    # print(month_name)

    # formatted_date = date_object.strftime("%d {0} %Y".format(month_name))
    # print(formatted_date)  # Output: 20 марта 2024


    import calendar

    # Создаем словарь с названиями месяцев на русском языке
    months = {
        1: 'января',
        2: 'февраля',
        3: 'марта',
        4: 'апреля',
        5: 'мая',
        6: 'июня',
        7: 'июля',
        8: 'августа',
        9: 'сентября',
        10: 'октября',
        11: 'ноября',
        12: 'декабря'
    }
    date_object = datetime.strptime(str(order.date_akt), '%Y-%m-%d').date()
    date_string = str(date_object)
    date_parts = date_string.split('-')
    year = int(date_parts[0])
    month = int(date_parts[1])
    day = int(date_parts[2])

    # Получаем название месяца на русском языке
    month_name = months[month]

    formatted_date = f"«{day}» {month_name} {year}"
    print(formatted_date)  # Output: 20 марта 2024








    doc = DocxTemplate("example.docx")
    context = { 'number' : document_data.reestr_oferts, 
               'fio': order.fio, 
               'fio_short': fio_short,
               'initials_order': initials_order,
               'changed_fio': changed_fio,
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
               'initials': initials,
               'document_issuing_authority': document_data.document_issuing_authority,
               'date_akt': formatted_date
               }
    doc.render(context)

    import time 
    # time.sleep(4)

    doc.save(f"dox/{filial.directory}/{order.number_orders_vozm}.docx")
    
    return("Готов отчет.")