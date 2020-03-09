from datetime import datetime

import pytz
from django.http import JsonResponse
from requests import Response
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
    result_code = request.data['Body']['stkCallback']['ResultCode']
    if result_code == 0:
        merchant_request_id = request.data['Body']['stkCallback']['MerchantRequestID']
        checkout_request_id = request.data['Body']['stkCallback']['CheckoutRequestID']
        result_description = request.data['Body']['stkCallback']['ResultDesc']
        amount = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value']
        mpesa_receipt_number = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value']
        transaction_date = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][2]['Value']
        phone_number = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][3]['Value']

        str_transaction_date = str(transaction_date)
        transaction_datetime = datetime.strptime(str_transaction_date, "%Y%m%d%H%M%S")
        timezone_transaction_datetime = pytz.timezone(transaction_datetime)

        our_model = LipaNaMpesaOnline.objects.create(
            merchant_request_id=merchant_request_id,
            checkout_request_id=checkout_request_id,
            result_code=result_code,
            result_description=result_description,
            amount=amount,
            mpesa_receipt_number=mpesa_receipt_number,
            mpesa_transaction_date=timezone_transaction_datetime,
            phone_number=phone_number
        )

        our_model.save()
        return Response({"OurResultDescription": "yey it worked"})
    return JsonResponse({'Result Code': result_code})
