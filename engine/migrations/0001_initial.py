# Generated by Django 4.0.2 on 2024-02-29 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exicuters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(blank=True, max_length=128, verbose_name='ФИО исполнителя')),
            ],
        ),
        migrations.CreateModel(
            name='Filials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Филиал')),
            ],
        ),
        migrations.CreateModel(
            name='Reestr_oferts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_orders_vozm', models.CharField(db_index=True, max_length=20, verbose_name='Номер договора возм.')),
                ('fio', models.CharField(max_length=128, verbose_name='ФИО')),
                ('date_orders', models.DateField(auto_now_add=True, verbose_name='Дата договора')),
                ('date_akt', models.DateField(auto_now_add=True, verbose_name='Дата акта')),
                ('price', models.FloatField(max_length=10, verbose_name='Цена')),
                ('date_buhgt', models.DateField(verbose_name='Дата передачи в бухгалтерию')),
                ('comment', models.CharField(max_length=512, verbose_name='Комментарий')),
                ('exicutor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='engine.exicuters', verbose_name='Исполнитель')),
                ('filial', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='engine.filials', verbose_name='Филиал')),
            ],
        ),
        migrations.AddField(
            model_name='exicuters',
            name='filial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='engine.filials', verbose_name='Филиал к котрому привязан исполнитель'),
        ),
    ]
