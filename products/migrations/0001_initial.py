# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('stock', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('CAFETERAPIA', 'Cafeterapia'), ('FITOTERAPIA', 'Fitoterapia'), ('HIALUR\xd3NICO', 'Hialur\xf3nico'), ('LINEA_ESENCIAL', 'L\xednea esencial'), ('LINFODRENANTE', 'Linfodrenante'), ('PERLAS', 'Perlas'), ('PIELES_GRASAS', 'Pieles grasas'), ('UNCATEGORIZED', 'Sin categorizar')], default='UNCATEGORIZED', max_length=255)),
            ],
        ),
    ]
