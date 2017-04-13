# -*- coding: utf-8 -*-
from datetime import datetime
from django.test import TestCase
from .models import Appointment, APPOINTMENT_STATES
from services.models import Service, CATEGORIES
from clients.models import Client, PARTNER_OPTIONS, KNOWN_FOR_CHOICES, LOPD_CHANNEL_CHOICES, LOPD_OPTION_CHOICES
from .models import Invoice


class AppointmentsTests(TestCase):
    def setUp(self):
        Appointment.objects.create(
            id=1,
            service=Service.objects.get(name='Maquillaje día'),
            date=datetime.now(),
            client=Client.objects.get(dni='12345678t'),
            state=APPOINTMENT_STATES.PENDING,
            invoice=Invoice.objects.get(id=1),
            notes='Test'
        )

        Service.objects.create(
            name='Maquillaje día',
            price=15.00,
            duration=900,
            category=CATEGORIES.FOTODEPILACION,
            description='¿Eres de maquillaje natural o tienes poco tiempo? Entonces esto es para tí, para cualquier ocasión, un toque de luz en tu rostro, un delineado suave, color en tus labios ¡y listo!'
        )

        Client.objects.create(
          dni='12345678t',
          name='Ander',
          surname='Conal',
          second_surname='Fuertes',
          birthdate=datetime.now(),
          phone_number='666666666',
          address='Fake Street, 7',
          postal_code='66666',
          city='Bilbao',
          province='Vizcaya',
          email='ander.conal@gmail.com',
          release_date=datetime.now(),
          partner=PARTNER_OPTIONS.NO_PARTNER,
          partner_release_date=datetime.now(),
          known_for=KNOWN_FOR_CHOICES.FACEBOOK,
          lopd=True,
          lopd_channel=LOPD_CHANNEL_CHOICES.WHATSAPP,
          lopd_options=LOPD_OPTION_CHOICES.FOTODEPILACION,
          notes='Test'
        )

        Invoice.objects.create(
            id=1,
            issueDate=datetime.now(),
            client=Client.objects.get(dni='12345678t')
        )

        def test_string_representation(self):
            """
            String representation of Appointment model should be:
            Appointment: (Appointment ID)
            """
            test_appointment = Appointment.objects.get(id=1)

            self.assertEqual(str(test_appointment), 'Appointment: ' + 
                             test_appointment.id)
