# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 16:00
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=9, unique=True)),
                ('name', models.CharField(max_length=35)),
                ('surname', models.CharField(max_length=35)),
                ('second_surname', models.CharField(max_length=35)),
                ('birthdate', models.DateField()),
                ('postal_code', models.CharField(max_length=5)),
                ('release_date', models.DateField()),
                ('partner', models.CharField(choices=[(0, 'No partner'), (1, 'Tipo A'), (2, 'Tipo B'), (3, 'Tipo C')], default=0, max_length=35)),
                ('known_for', models.CharField(choices=[(0, 'Facebook'), (1, 'Instagram'), (2, 'Internet'), (3, 'Radio'), (4, 'Boca a boca'), (5, 'Localizaci\xf3n'), (6, 'Publicidad impresa'), (7, 'Otros')], default=0, max_length=35)),
                ('lopd_channel', models.CharField(choices=[(0, 'WhatsApp'), (1, 'Email')], default=0, max_length=35)),
                ('lopd_options', multiselectfield.db.fields.MultiSelectField(choices=[(0, 'Fotodepilaci\xf3n'), (1, 'Manicura'), (2, 'Pedicura'), (3, 'Maquillaje'), (4, 'Tratamientos faciales'), (5, 'Tratamientos corporales'), (6, 'Cejas y pesta\xf1as')], max_length=13)),
            ],
        ),
    ]
