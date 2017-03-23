# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 08:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='invoice',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoices.Invoice'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
