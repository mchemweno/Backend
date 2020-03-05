from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .serializers import *
from .models import LipaNaMpesaOnline


# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def LipaNaMpesaCallBackURLView(request):
    """
    mpesa response format
    {'Body':
        {'stkCallback':
            {'MerchantRequestID': '13852-17960109-1',
            'CheckoutRequestID': 'ws_CO_050320201800153964',
            'ResultCode': 0,
            'ResultDesc': 'The service request is processed successfully.',
            'CallbackMetadata':
                        {'Item': [
                                {'Name': 'Amount', 'Value': 5.0},
                                {'Name': 'MpesaReceiptNumber', 'Value': 'OC54JS5822'},
                                {'Name': 'TransactionDate', 'Value': 20200305180032},
                                {'Name': 'PhoneNumber', 'Value': 254726990002}]}
                        }
            }
        }
    }
    {'Body': {'stkCallback': {'MerchantRequestID': '2833-18031737-1', 'CheckoutRequestID': 'ws_CO_050320201840364733',
                              'ResultCode': 0, 'ResultDesc': 'The service request is processed successfully.',
                              'CallbackMetadata': {'Item': [{'Name': 'Amount', 'Value': 1.0},
                                                            {'Name': 'MpesaReceiptNumber', 'Value': 'OC54JTU4S4'},
                                                            {'Name': 'TransactionDate', 'Value': 20200305184050},
                                                            {'Name': 'PhoneNumber', 'Value': 254726990002}]}}}}


    """
    print(request.data)

    merchant_request_id = request.data['Body']['stkCallback']['MerchantRequestID']
    print(merchant_request_id, "this should be merachant request id")
    checkout_request_id = request.data['Body']['stkCallback']['CheckoutRequestID']
    result_code = request.data['Body']['stkCallback']['ResultCode']
    result_description = request.data['Body']['stkCallback']['ResultDesc']
    amount = request.data['Body']['stkCallback']['CallBackMetadata']['Item'][0]['Value']
    print(amount, 'this should be amount')
    mpesa_receipt_number = request.data['Body']['stkCallback']['CallBackMetadata']['Item'][1]['Value']
    print(mpesa_receipt_number, "this is mpesa receipt number")
    transaction_date = request.data['Body']['stkCallback']['CallBackMetadata']['Item'][2]['Value']
    print(transaction_date, 'This is the transaction date')
    transaction_date = request.data['Body']['stkCallback']['CallBackMetadata']['Item'][3]['Value']
    print(transaction_date, 'this is the phone number')
