# Generated by Django 4.0.2 on 2024-03-12 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0008_exicuters_position_filial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filials',
            name='directory',
            field=models.CharField(default='/', max_length=128, verbose_name='Директория договоров филиала'),
        ),
    ]
