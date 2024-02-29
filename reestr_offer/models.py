from django.db import models
from engine.models import Exicuters

# Create your models here.

class LocalOfferCreate(models.Model):
    name_local = models.CharField(max_length=255, blank=False, verbose_name='Населенный пункт')


class ExicutorOffer(models.Model):
    fio = models.CharField(max_length=255, blank=True, verbose_name='ФИО исполнителя')
    local = models.ForeignKey(LocalOfferCreate, on_delete=models.PROTECT, verbose_name='Населенный пункт')


class RegisterByOffer(models.Model):
    num_offers = models.CharField(max_length=128, blank=True, verbose_name='Номер договора')
    fio_customer = models.CharField(max_length=256, blank=True, verbose_name='ФИО заказчика')
    local = models.ForeignKey(LocalOfferCreate, on_delete=models.PROTECT, verbose_name='Населенный пункт')
    name_service = models.CharField(max_length=512, blank=True, verbose_name='Наименование услуги')
    date_akt = models.DateField(blank=True, verbose_name='Дата акта')

    price = models.FloatField(blank=True, verbose_name='Цена')
    exicutor = models.ForeignKey(ExicutorOffer, on_delete=models.PROTECT, verbose_name='Исполнитель')
    date_buhgt = models.DateField(blank=True, verbose_name='Дата передачи в бухгалтерию')
    comment = models.CharField(max_length=512, blank=False, verbose_name='Примечание')



