#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Set UTF-8 enconding """

from __future__ import unicode_literals
from django.db import models
from model_utils import Choices
from clients.models import Client

PRODUCT_CATEGORIES = Choices(
    ('CAFETERAPIA', 'Cafeterapia'),
    ('FITOTERAPIA', 'Fitoterapia'),
    ('HIALURÓNICO', 'Hialurónico'),
    ('LINEA_ESENCIAL', 'Línea esencial'),
    ('LINFODRENANTE', 'Linfodrenante'),
    ('PERLAS', 'Perlas'),
    ('PIELES_GRASAS', 'Pieles grasas'),
    ('PIELES_SENSIBLES', 'Pieles sensibles'),
    ('METODOS_DE_PAGO', 'Métodos de pago'),
    ('UNCATEGORIZED', 'Sin categorizar')
)


class Product(models.Model):
    """ Product model. """
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField(default=0)
    category = models.CharField(
        choices=PRODUCT_CATEGORIES,
        default=PRODUCT_CATEGORIES.UNCATEGORIZED,
        max_length=255
    )

    def __unicode__(self):
        return self.name

class PrepaidCard(Product):
    """ Payment Method model. Multi-table inheritance. """
    available_amount = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    client = models.OneToOneField(
        Client,
        on_delete=models.CASCADE
    )

    def __unicode__(self):
        return self.name
