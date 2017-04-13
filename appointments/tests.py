# -*- coding: utf-8 -*-

from django.test import TestCase
from .models import Appointment
from .models import Service


class AppointmentsTests(TestCase):
    def setUp(self):
        Appointment.objects.create(

        )

        Service.objects.create(

        )
