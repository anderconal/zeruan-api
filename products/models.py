#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Set UTF-8 enconding """

from __future__ import unicode_literals
from django.db import models
from multiselectfield import MultiSelectField

class Product(models.Model):
  """ Product model. """