#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Set UTF-8 enconding """

from __future__ import unicode_literals
from django.db import models
from services.models import Service
from products.models import Product
from invoices.models import Invoice
from model_utils import Choices
from django.utils.translation import gettext as _

VAT_CHOICES = Choices(
    (21, 'GENERAL', _('GENERAL')),
    (10, 'REDUCIDO', _('REDUCIDO')),
    (4, 'SUPERREDUCIDO', _('SUPERREDUCIDO')),
    (0, 'EXENTO', _('EXENTO'))
)


class InvoiceDetail(models.Model):
    """ InvoiceDetail model. """
    invoice = models.OneToOneField(
        Invoice,
        on_delete=models.CASCADE,
        primary_key=True)
    service = models.ManyToManyField(Service, blank=True, null=True)
    product = models.ManyToManyField(Product, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    vat = models.IntegerField(
        choices=VAT_CHOICES,
        default=VAT_CHOICES.GENERAL
    )
    discount = models.IntegerField(default=0)
