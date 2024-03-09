# Generated by Django 5.0.2 on 2024-03-09 14:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0004_alter_filials_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Территория исполнения')),
            ],
        ),
        migrations.AlterField(
            model_name='reestr_oferts',
            name='comment',
            field=models.CharField(blank=True, max_length=512, verbose_name='Комментарий'),
        ),
        migrations.CreateModel(
            name='Contract_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification_document', models.CharField(blank=True, max_length=256)),
                ('passport_series', models.CharField(blank=True, max_length=4, verbose_name='Серия паспорта')),
                ('number_passport', models.CharField(blank=True, max_length=6, verbose_name='Номер паспорта')),
                ('document_issue_date', models.DateField(blank=True, default='20.10.2024', verbose_name='Дата выдачи документа')),
                ('document_issuing_authority', models.CharField(blank=True, max_length=512, verbose_name='Кем выдан документ')),
                ('adress', models.CharField(blank=True, max_length=512, verbose_name='Адрес')),
                ('reestr_oferts', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='engine.reestr_oferts', verbose_name='Связанный договор')),
                ('location', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.PROTECT, to='engine.location', verbose_name='Территория исполнения')),
            ],
        ),
    ]