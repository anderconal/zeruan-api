#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Set UTF-8 enconding """

from __future__ import unicode_literals
from django.db import models
from multiselectfield import MultiSelectField
from model_utils import Choices

PARTNER_OPTIONS = Choices(
    ('NO_PARTNER', 'No socio'),
    ('PARTNER_A', 'Tipo A'),
    ('PARTNER_B', 'Tipo B'),
    ('PARTNER_C', 'Tipo C')
)

KNOWN_FOR_CHOICES = Choices(
    ('FACEBOOK', 'Facebook'),
    ('INSTAGRAM', 'Instagram'),
    ('INTERNET', 'Internet'),
    ('RADIO', 'Radio'),
    ('BOCA_A_BOCA', 'Boca a boca'),
    ('LOCALIZACION', 'Localización'),
    ('PUBLICIDAD_IMPRESA', 'Publicidad impresa'),
    ('OTROS', 'Otros')
)

LOPD_CHANNEL_CHOICES = Choices(
    ('WHATSAPP', 'WhatsApp'),
    ('EMAIL', 'Email')
)

LOPD_OPTION_CHOICES = Choices(
    ('FOTODEPILACION', 'Fotodepilación'),
    ('MANICURA', 'Manicura'),
    ('PEDICURA', 'Pedicura'),
    ('MAQUILLAJE', 'Maquillaje'),
    ('TRATAMIENTOS_FACIALES', 'Tratamientos faciales'),
    ('TRATAMIENTOS_CORPORALES', 'Tratamientos corporales'),
    ('CEJAS_Y_PESTANAS', 'Cejas y pestañas')
)

class Client(models.Model):
    """ Client model. """
    dni = models.CharField(max_length=9, unique=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    second_surname = models.CharField(max_length=255)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    phone_number = models.CharField(max_length=21)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    partner = models.CharField(
        choices=PARTNER_OPTIONS,
        default=PARTNER_OPTIONS.NO_PARTNER,
        max_length=255
    )
    partner_release_date = models.DateField(auto_now=False, auto_now_add=False)
    known_for = models.CharField(
        choices=KNOWN_FOR_CHOICES,
        default=KNOWN_FOR_CHOICES.FACEBOOK,
        max_length=255
    )
    lopd = models.BooleanField(default=False)
    lopd_channel = models.CharField(
        choices=LOPD_CHANNEL_CHOICES,
        default=LOPD_CHANNEL_CHOICES.WHATSAPP,
        max_length=255
    )
    lopd_options = MultiSelectField(
        choices=LOPD_OPTION_CHOICES,
        default=None,
        max_length=255
    )
    notes = models.TextField()
