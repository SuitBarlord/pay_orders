# Generated by Django 4.0.2 on 2024-02-29 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExicutorOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(blank=True, max_length=255, verbose_name='ФИО исполнителя')),
            ],
        ),
        migrations.CreateModel(
            name='LocalOfferCreate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_local', models.CharField(max_length=255, verbose_name='Населенный пункт')),
            ],
        ),
        migrations.CreateModel(
            name='RegisterByOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_offers', models.CharField(blank=True, max_length=128, verbose_name='Номер договора')),
                ('fio_customer', models.CharField(blank=True, max_length=256, verbose_name='ФИО заказчика')),
                ('name_service', models.CharField(blank=True, max_length=512, verbose_name='Наименование услуги')),
                ('date_akt', models.DateField(blank=True, verbose_name='Дата акта')),
                ('price', models.FloatField(blank=True, verbose_name='Цена')),
                ('date_buhgt', models.DateField(blank=True, verbose_name='Дата передачи в бухгалтерию')),
                ('comment', models.CharField(max_length=512, verbose_name='Примечание')),
                ('exicutor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reestr_offer.exicutoroffer', verbose_name='Исполнитель')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reestr_offer.localoffercreate', verbose_name='Населенный пункт')),
            ],
        ),
        migrations.AddField(
            model_name='exicutoroffer',
            name='local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reestr_offer.localoffercreate', verbose_name='Населенный пункт'),
        ),
    ]