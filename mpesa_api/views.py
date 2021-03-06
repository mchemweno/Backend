from datetime import datetime, timezone

import pytz
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

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
        transaction_date = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][3]['Value']
        phone_number = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value']

        str_transaction_date = str(transaction_date)
        transaction_datetime = datetime.strptime(str_transaction_date, "%Y%m%d%H%M%S")
        datetime_nairobi_timezone = pytz.timezone('Africa/Nairobi').localize(transaction_datetime)

        our_model = LipaNaMpesaOnline.objects.create(
            merchant_request_id=merchant_request_id,
            checkout_request_id=checkout_request_id,
            result_code=result_code,
            result_description=result_description,
            amount=amount,
            mpesa_receipt_number=mpesa_receipt_number,
            mpesa_transaction_date=datetime_nairobi_timezone,
            phone_number=phone_number
        )

        our_model.save()
        return JsonResponse({"OurResultDescription": "yey it worked"})
    print(f'Result Code : {result_code}')
    return JsonResponse({'Result Code': result_code})


@api_view(['POST'])
@permission_classes([AllowAny])
def C2bValidationURLView(request):
    print(request.data, ' this is the request data validation.')
    return JsonResponse({'ResultCode': 0})


@api_view(['POST'])
@permission_classes([AllowAny])
def C2bConfirmationURLView(request):
    """
    {'TransactionType': 'Pay Bill',
    'TransID': 'OC941HBFM8',
    'TransTime': '20200309193038',
    'TransAmount': '2.00',
     'BusinessShortCode': '600119',
     'BillRefNumber': '1234567',
     'InvoiceNumber': '',
     'OrgAccountBalance': '150665.00',
     'ThirdPartyTransID': '1234567890',
     'MSISDN': '254708374149',
     'FirstName': 'John',
     'MiddleName': 'J.',
     'LastName': 'Doe'}
    """
    print(request.data, ' this is the request data confirmation.')
    data = request.data
    serializer = C2BPaymentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=201)
    return Response(status=404)
