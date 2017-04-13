# -*- coding: utf-8 -*-
from datetime import datetime

from django.test import TestCase
from .models import Client
from .models import PARTNER_OPTIONS, KNOWN_FOR_CHOICES, LOPD_CHANNEL_CHOICES, LOPD_OPTION_CHOICES


class ClientTests(TestCase):
    def setUp(self):
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

    def test_string_representation(self):
        """
        String representation of Client model should be:
        name (white space) surname (white space) second_surname
        """
        test_client = Client.objects.get(dni='12345678t')

        self.assertEqual(str(test_client), test_client.name + ' ' +
                         test_client.surname + ' ' +
                         test_client.second_surname)

    def test_verbose_name_plural(self):
        """
        The pluralization of Client should be Clients
        """
        self.assertEqual(str(Client._meta.verbose_name_plural), 'clients')
