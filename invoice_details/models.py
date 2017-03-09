#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Set UTF-8 enconding """

from __future__ import unicode_literals
from django.db import models
from multiselectfield import MultiSelectField
from services.models import Service
from products.models import Product
from invoices.models import Invoice
from model_utils import Choices

VAT_CHOICES = Choices(
    ('GENERAL', 21),
    ('REDUCIDO', 10),
    ('SUPERREDUCIDO', 4),
    ('EXENTO', 0),
    ('SIN IVA', 0)
)

class InvoiceDetail(models.Model):
    """ InvoiceDetail model. """
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, primary_key=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    vat = models.IntegerField(
        choices=VAT_CHOICES,
        default=VAT_CHOICES.GENERAL,
        max=VAT_CHOICES.GENERAL
    )
    discount = models.IntegerField(default=0)
