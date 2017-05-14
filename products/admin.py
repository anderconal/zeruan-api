from django.contrib import admin

from .models import Product
from .models import PrepaidCard

admin.site.register(Product)
admin.site.register(PrepaidCard)
