from datetime import datetime
from django.test import TestCase

from services.models import Service, CATEGORIES
from products.models import Product, PRODUCT_CATEGORIES
from clients.models import Client, PARTNER_OPTIONS, KNOWN_FOR_CHOICES, LOPD_CHANNEL_CHOICES, LOPD_OPTION_CHOICES
from invoices.models import Invoice
from .models import InvoiceDetail, VAT_CHOICES


class InvoiceDetailTests(TestCase):
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

        Invoice.objects.create(
            issueData=datetime.now(),
            client=Client.objects.get(dni='12345678t')
        )

        Service.objects.create(
            name='Maquillaje día',
            price=15.00,
            duration=900,
            category=CATEGORIES.FOTODEPILACION,
            description='¿Eres de maquillaje natural o tienes poco tiempo? Entonces esto es para tí, para cualquier ocasión, un toque de luz en tu rostro, un delineado suave, color en tus labios ¡y listo!'
        )

        Product.objects.create(
            name='Leche',
            price=25.80,
            stock=1,
            category=PRODUCT_CATEGORIES.PIELES_SENSIBLES
        )

        InvoiceDetail.objects.create(
            invoice=Invoice.objects.get(
                client=Client.objects.get(dni='12345678t')
            ),
            service=Service.objects.get(
                name='Maquillaje día'
            ),
            product=Product.objects.get(
                name='Leche'
            ),
            quantity=1,
            vat=VAT_CHOICES.GENERAL,
            discount=0
        )

        def test_string_representation(self):
            """
            String representation of InvoiceDetails model shoudl be:
            Invoice: invoice.id Invoice Detail: invoice_detail.id
            """
            test_invoice_detail = InvoiceDetail.objects.get(
                invoice=Invoice.objects.get(
                    client=Client.objects.get(dni='12345678t')
                )
            )

            self.assertEqual(str(test_invoice_detail), 'Invoice: ' + test_invoice_detail.invoice.id + 
                             ' Invoice Detail: ' + test_invoice_detail.id)
