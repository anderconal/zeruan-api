# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 16:49
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.CharField(default=None, max_length=35),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='city',
            field=models.CharField(default=None, max_length=35),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.CharField(default=None, max_length=35),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='lopd',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='client',
            name='notes',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='phone_number',
            field=models.CharField(default=None, max_length=21),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='province',
            field=models.CharField(default=None, max_length=35),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='known_for',
            field=models.CharField(choices=[('FACEBOOK', 'Facebook'), ('INSTAGRAM', 'Instagram'), ('INTERNET', 'Internet'), ('RADIO', 'Radio'), ('BOCA_A_BOCA', 'Boca a boca'), ('LOCALIZACION', 'Localizaci\xf3n'), ('PUBLICIDAD_IMPRESA', 'Publicidad impresa'), ('OTROS', 'Otros')], default='FACEBOOK', max_length=35),
        ),
        migrations.AlterField(
            model_name='client',
            name='lopd_channel',
            field=models.CharField(choices=[('WHATSAPP', 'WhatsApp'), ('EMAIL', 'Email')], default='WHATSAPP', max_length=35),
        ),
        migrations.AlterField(
            model_name='client',
            name='lopd_options',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('FOTODEPILACION', 'Fotodepilaci\xf3n'), ('MANICURA', 'Manicura'), ('PEDICURA', 'Pedicura'), ('MAQUILLAJE', 'Maquillaje'), ('TRATAMIENTOS_FACIALES', 'Tratamientos faciales'), ('TRATAMIENTOS_CORPORALES', 'Tratamientos corporales'), ('CEJAS_Y_PESTANAS', 'Cejas y pesta\xf1as')], default=None, max_length=35),
        ),
        migrations.AlterField(
            model_name='client',
            name='partner',
            field=models.CharField(choices=[('NO_PARTNER', 'No socio'), ('PARTNER_A', 'Tipo A'), ('PARTNER_B', 'Tipo B'), ('PARTNER_C', 'Tipo C')], default='NO_PARTNER', max_length=35),
        ),
    ]
