# Generated by Django 4.0.2 on 2024-03-14 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0011_remove_contract_data_document_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reestr_oferts',
            name='number_orders_vozm',
            field=models.CharField(db_index=True, max_length=20, unique=True, verbose_name='Номер договора возм.'),
        ),
    ]
