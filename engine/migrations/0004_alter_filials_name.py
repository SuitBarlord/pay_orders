# Generated by Django 4.0.2 on 2024-03-05 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0003_alter_exicuters_fio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filials',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Филиал'),
        ),
    ]