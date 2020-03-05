from datetime import datetime

from django.db import models


# Create your models here.
class LipaNaMpesaOnline(models.Model):
    merchant_request_id = models.CharField(max_length=70)
    checkout_request_id = models.CharField(max_length=50)
    result_code = models.IntegerField()
    result_description = models.CharField(max_length=120)
    amount = models.FloatField()
    mpesa_receipt_number = models.CharField(max_length=30)
    mpesa_transaction_date = models.DateTimeField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.mpesa_receipt_number + ' ' + str(self.amount) + ' ' + self.phone_number
