# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_details', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicedetail',
            name='vat',
            field=models.IntegerField(choices=[('GENERAL', 21), ('REDUCIDO', 10), ('SUPERREDUCIDO', 4), ('EXENTO', 0), ('SIN IVA', 0)], default='GENERAL'),
        ),
    ]