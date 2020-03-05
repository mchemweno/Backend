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

    """
    print(request.data)

    merchant_request_id = request.data['Body']['stkCallback']['MerchantRequestID']
    print(merchant_request_id, "this should be merachant request id")

