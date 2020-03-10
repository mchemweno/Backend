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


class C2BPayment(models.Model):
    TransactionType = models.CharField(max_length=20)
    TransID = models.CharField(max_length=15)
    TransTime = models.CharField(max_length=14)
    TransAmount = models.CharField(max_length=10)
    BusinessShortCode = models.CharField(max_length=8)
    BillRefNumber = models.CharField(max_length=20)
    InvoiceNumber = models.CharField(max_length=20, blank=True)
    OrgAccountBalance = models.CharField(max_length=12)
    ThirdPartyTransID = models.CharField(max_length=20, blank=True)
    MSISDN = models.CharField(max_length=12)
    FirstName = models.CharField(max_length=20)
    MiddleName = models.CharField(max_length=20, blank=True)
    LastName = models.CharField(max_length=20)

    def __str__(self):
        return self.TransID + ' ' + str(self.TransAmount) + ' ' + self.MSISDN
