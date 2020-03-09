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


class C2BPayments(models.Model):
    TransactionType = models.CharField(max_length=20, blank=True)
    TransID = models.CharField(max_length=15, blank=True)
    TransTime = models.CharField(max_length=14, blank=True)
    TransAmount = models.CharField(max_length=10, blank=True)
    BusinessShortCode = models.CharField(max_length=8, blank=True)
    BillRefNumber = models.CharField(max_length=20, blank=True)
    InvoiceNumber = models.CharField(max_length=20, blank=True)
    OrgAccountBalance = models.CharField(max_length=12, blank=True)
    ThirdPartyTransID = models.CharField(max_length=20, blank=True)
    MSISDN = models.CharField(max_length=12, blank=True)
    FirstName = models.CharField(max_length=20, blank=True)
    MiddleName = models.CharField(max_length=20, blank=True)
    LastName = models.CharField(max_length=20, blank=True)
