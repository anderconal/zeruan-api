#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Set UTF-8 enconding """

from __future__ import unicode_literals
from django.db import models
from services.models import Service
from products.models import Product
from invoices.models import Invoice
from model_utils import Choices

VAT_CHOICES = Choices(
    (21, 21),
    (10, 10),
    (4, 4),
    (0, 0)
)

class InvoiceDetail(models.Model):
    """ InvoiceDetail model. """
    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE, primary_key=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    vat = models.IntegerField(
        choices=VAT_CHOICES,
        default=21
    )
    discount = models.IntegerField(default=0)
