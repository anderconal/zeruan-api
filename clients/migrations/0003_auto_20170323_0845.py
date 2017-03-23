# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 08:45
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20170323_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='dni',
            field=models.CharField(blank=True, max_length=9, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='lopd_options',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('FOTODEPILACION', 'Fotodepilaci\xf3n'), ('MANICURA', 'Manicura'), ('PEDICURA', 'Pedicura'), ('MAQUILLAJE', 'Maquillaje'), ('TRATAMIENTOS_FACIALES', 'Tratamientos faciales'), ('TRATAMIENTOS_CORPORALES', 'Tratamientos corporales'), ('CEJAS_Y_PESTANAS', 'Cejas y pesta\xf1as')], default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='postal_code',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='province',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='second_surname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
