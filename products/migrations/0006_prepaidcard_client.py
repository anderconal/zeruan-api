# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 22:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20170413_2224'),
        ('products', '0005_auto_20170514_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='prepaidcard',
            name='client',
            field=models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to='clients.Client'),
            preserve_default=False,
        ),
    ]