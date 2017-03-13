# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CAFETERAPIA', 'Cafeterapia'), ('FITOTERAPIA', 'Fitoterapia'), ('HIALUR\xd3NICO', 'Hialur\xf3nico'), ('LINEA_ESENCIAL', 'L\xednea esencial'), ('LINFODRENANTE', 'Linfodrenante'), ('PERLAS', 'Perlas'), ('PIELES_GRASAS', 'Pieles grasas'), ('UNCATEGORIZED', 'Sin categorizar')], default='UNCATEGORIZED', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
