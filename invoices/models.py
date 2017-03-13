#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Set UTF-8 enconding """

from __future__ import unicode_literals
from django.db import models
from clients.models import Client


class Invoice(models.Model):
    """ Invoice model. """
    issueDate = models.DateField(auto_now=False, auto_now_add=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
