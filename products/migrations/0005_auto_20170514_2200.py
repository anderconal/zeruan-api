# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 22:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20170514_2125'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PaymentMethod',
            new_name='PrepaidCard',
        ),
    ]