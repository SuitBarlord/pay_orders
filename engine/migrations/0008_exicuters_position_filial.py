# Generated by Django 4.0.2 on 2024-03-11 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0007_alter_contract_data_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='exicuters',
            name='position_filial',
            field=models.CharField(default='Администратор', max_length=128, verbose_name='Должность'),
        ),
    ]
