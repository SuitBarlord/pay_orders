from django.db import models

# Create your models here.





class Filials(models.Model):
    name = models.CharField(max_length=128, verbose_name='Филиал')
    def __str__(self):
        return self.name



class Exicuters(models.Model):
    fio = models.CharField(max_length=128, blank=False, verbose_name='ФИО исполнителя')
    position_filial = models.CharField(max_length=128, blank=False, default='Администратор', verbose_name='Должность')
    filial = models.ForeignKey(Filials, on_delete=models.PROTECT, verbose_name='Филиал к котрому привязан исполнитель')
    def __str__(self):
        return self.fio



class Reestr_oferts(models.Model):

    number_orders_vozm = models.CharField(max_length=20, blank=False, verbose_name='Номер договора возм.', db_index=True)
    fio = models.CharField(max_length=128, blank=False, verbose_name='ФИО')
    date_orders = models.DateField(auto_now_add=True, verbose_name='Дата договора')

    date_akt = models.DateField(auto_now_add=True, verbose_name='Дата акта')
    exicutor = models.ForeignKey(Exicuters, on_delete=models.PROTECT, verbose_name='Исполнитель')
    filial = models.ForeignKey(Filials, on_delete=models.PROTECT, verbose_name='Филиал')
    price = models.FloatField(max_length=10, verbose_name='Цена')
    date_buhgt = models.DateField(verbose_name='Дата передачи в бухгалтерию')
    comment = models.CharField(max_length=512, verbose_name='Комментарий', blank=True)
    
    def __str__(self) -> str:
        return self.number_orders_vozm
    
    
class Location(models.Model):
    name = models.CharField(max_length=128, verbose_name='Территория исполнения')
    
    def __str__(self):
        return self.name
    
    
class Contract_Data(models.Model):
    reestr_oferts = models.OneToOneField(Reestr_oferts, on_delete=models.PROTECT, verbose_name='Связанный договор')
    identification_document = models.CharField(max_length=256, blank=True, verbose_name='Индификационный документ')
    passport_series = models.CharField(max_length=4, blank=True, verbose_name='Серия паспорта')
    number_passport = models.CharField(max_length=6, blank=True, verbose_name='Номер паспорта')
    document_issue_date = models.DateField(blank=True, verbose_name='Дата выдачи документа', default='20.10.2024')
    document_issuing_authority = models.CharField(max_length=512, blank=True, verbose_name='Кем выдан документ')
    location = models.ForeignKey(Location, on_delete=models.PROTECT, blank=True, verbose_name='Территория исполнения')
    adress = models.CharField(max_length=512, blank=True, verbose_name='Адрес')
    

    
    



