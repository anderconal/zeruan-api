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
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('duration', models.IntegerField(default=900)),
                ('category', models.CharField(choices=[('FOTODEPILACION', 'Fotodepilaci\xf3n'), ('MANICURA', 'Manicura'), ('PEDICURA', 'Pedicura'), ('MAQUILLAJE', 'Maquillaje'), ('TRATAMIENTOS_FACIALES', 'Tratamientos faciales'), ('TRATAMIENTOS_CORPORALES', 'Tratamientos corporales'), ('CEJAS_Y_PESTANAS', 'Cejas y pesta\xf1as')], default='FOTODEPILACION', max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
