from django.contrib import admin

# Register your models here.
from .models import LipaNaMpesaOnline, C2BPayments

admin.site.register(LipaNaMpesaOnline)
admin.site.register(C2BPayments)
