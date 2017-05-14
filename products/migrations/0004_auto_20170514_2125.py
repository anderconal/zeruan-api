# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 21:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='available_amount',
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.Product')),
                ('available_amount', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
            bases=('products.product',),
        ),
    ]
