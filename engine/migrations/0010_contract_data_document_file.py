# Generated by Django 4.0.2 on 2024-03-13 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0009_filials_directory'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract_data',
            name='document_file',
            field=models.FileField(blank=True, upload_to='', verbose_name='Печатный документ'),
        ),
    ]