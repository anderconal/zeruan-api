# -*- coding: utf-8 -*-

from django.test import TestCase
from django.utils import timezone
from clients.models import Client, PARTNER_OPTIONS, KNOWN_FOR_CHOICES, LOPD_CHANNEL_CHOICES, LOPD_OPTION_CHOICES
from services.models import Service, CATEGORIES
from invoices.models import Invoice
from .models import Appointment, APPOINTMENT_STATES


class AppointmentsTests(TestCase):
    """ Initial setUp for future tests """
    def setUp(self):
        self.client = Client.objects.create(
          dni='12345678t',
          name='Ander',
          surname='Conal',
          second_surname='Fuertes',
          birthdate=timezone.now(),
          phone_number='666666666',
          address='Fake Street, 7',
          postal_code='66666',
          city='Bilbao',
          province='Vizcaya',
          email='ander.conal@gmail.com',
          release_date=timezone.now(),
          partner=PARTNER_OPTIONS.NO_PARTNER,
          partner_release_date=timezone.now(),
          known_for=KNOWN_FOR_CHOICES.FACEBOOK,
          lopd=True,
          lopd_channel=LOPD_CHANNEL_CHOICES.WHATSAPP,
          lopd_options=LOPD_OPTION_CHOICES.FOTODEPILACION,
          notes='Test'
        )

        self.service = Service.objects.create(
            name='Maquillaje día',
            price=15.00,
            duration=900,
            category=CATEGORIES.FOTODEPILACION,
            description='¿Eres de maquillaje natural o tienes poco tiempo? Entonces esto es para tí, ' +
                        'para cualquier ocasión, un toque de luz en tu rostro, un delineado suave, ' +
                        'color en tus labios ¡y listo!'
        )

        self.invoice = Invoice.objects.create(
            issueDate=timezone.now(),
            client=self.client
        )

        self.appointment = Appointment.objects.create(
            service=self.service,
            date=timezone.now(),
            client=self.client,
            state=APPOINTMENT_STATES.PENDING,
            invoice=self.invoice,
            notes='Test'
        )
