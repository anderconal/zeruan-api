from django.test import TestCase
from .models import Client, PARTNER_OPTIONS, KNOWN_FOR_CHOICES, LOPD_CHANNEL_CHOICES
from datetime import datetime

# Create your tests here.
class ClientModelTest(TestCase):
  
  def setUp(self):
    self.client_data = dict(
      dni='78952767t',
      name='Ander',
      surname='Conal',
      second_surname='Fuertes',
      birthdate=datetime.now(),
      phone_number='666666666',
      address='Fake Street, 7',
      partner=PARTNER_OPTIONS.NO_PARTNER,
      known_for=KNOWN_FOR_CHOICES.FACEBOOK,
      lopd=True,
      lopd_channel=LOPD_CHANNEL_CHOICES.WHATSAPP
    )

  def test_client_create(self):
    Client.objects.create(**self.client_data)
    client = Client.objects.get(id=1)
    #self.assertIs(client.name, 'Ander')
    assert client.name == 'Ander'
