# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 22:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('invoices', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceDetail',
            fields=[
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='invoices.Invoice')),
                ('quantity', models.IntegerField(default=0)),
                ('vat', models.IntegerField(choices=[('GENERAL', 21), ('REDUCIDO', 10), ('SUPERREDUCIDO', 4), ('EXENTO', 0), ('SIN IVA', 0)], default='GENERAL', max_length='GENERAL')),
                ('discount', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Service')),
            ],
        ),
    ]