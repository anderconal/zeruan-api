# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 22:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20170514_2200'),
        ('invoice_details', '0005_auto_20170514_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicedetail',
            name='prepaid_card',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.PrepaidCard'),
        ),
    ]
