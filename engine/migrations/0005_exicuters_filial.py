# Generated by Django 4.1 on 2024-02-25 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0004_remove_filials_fio_exicutor_filial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exicuters',
            name='filial',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='engine.filials', verbose_name='Филиал к котрому привязан исполнитель'),
        ),
    ]
