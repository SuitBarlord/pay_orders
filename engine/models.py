from django.db import models

# Create your models here.




class Filials(models.Model):
    name = models.CharField(max_length=128, verbose_name='Филиал')
    fio_exicutor_filial = models.ForeignKey('Exicuters', blank=False, verbose_name='ФИО сотрудников привязанных к филиалу', on_delete=models.PROTECT)






class Exicuters(models.Model):
    fio = models.CharField(max_length=128, blank=True, verbose_name='ФИО исполнителя')
    def __str__(self):
        return self.fio



class Reestr_oferts(models.Model):

    number_orders_vozm = models.CharField(max_length=20, blank=False, verbose_name='Номер договора возм.', db_index=True)
    fio = models.CharField(max_length=128, blank=False, verbose_name='ФИО')
    date_orders = models.DateField(auto_now_add=True, verbose_name='Дата договора')

    date_akt = models.DateField(auto_now_add=True, verbose_name='Дата акта')
    exicutor = models.ForeignKey(Exicuters, on_delete=models.PROTECT, verbose_name='Исполнитель')
    price = models.FloatField(max_length=10, verbose_name='Цена')
    date_buhgt = models.DateField(verbose_name='Дата передачи в бухгалтерию')
    comment = models.CharField(max_length=512)
    



