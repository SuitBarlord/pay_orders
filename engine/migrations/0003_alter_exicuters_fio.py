# Generated by Django 4.0.2 on 2024-03-05 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0002_alter_filials_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exicuters',
            name='fio',
            field=models.CharField(max_length=128, verbose_name='ФИО исполнителя'),
        ),
    ]
