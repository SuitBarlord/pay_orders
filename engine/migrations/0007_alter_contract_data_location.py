# Generated by Django 4.0.2 on 2024-03-11 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0006_alter_contract_data_identification_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract_data',
            name='location',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='engine.location', verbose_name='Территория исполнения'),
        ),
    ]
