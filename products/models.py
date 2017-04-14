#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Set UTF-8 enconding """

from __future__ import unicode_literals
from django.db import models
from model_utils import Choices

PRODUCT_CATEGORIES = Choices(
    ('CAFETERAPIA', 'Cafeterapia'),
    ('FITOTERAPIA', 'Fitoterapia'),
    ('HIALURÓNICO', 'Hialurónico'),
    ('LINEA_ESENCIAL', 'Línea esencial'),
    ('LINFODRENANTE', 'Linfodrenante'),
    ('PERLAS', 'Perlas'),
    ('PIELES_GRASAS', 'Pieles grasas'),
    ('PIELES_SENSIBLES', 'Pieles sensibles'),
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
