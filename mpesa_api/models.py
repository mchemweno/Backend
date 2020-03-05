from datetime import datetime

from django.db import models


# Create your models here.
class LipaNaMpesaOnline(models.Model):
    merchant_request_id = models.CharField(max_length=70, default='h')
    checkout_request_id = models.CharField(max_length=50, default='h')
    result_code = models.IntegerField(default=0)
    result_description = models.CharField(max_length=120, default='h')
    amount = models.FloatField(default=0.0)
    mpesa_receipt_number = models.CharField(max_length=30, default='h')
    mpesa_transaction_date = models.DateTimeField(default=datetime.now())
    phone_number = models.CharField(max_length=15, default='h')
