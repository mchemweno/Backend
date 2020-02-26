import requests
import mpesa_keys
from access_token import generate_access_token
from encode import generate_password
from utils import get_timestamp


def lipa_na_mpesa():
    formatted_time = get_timestamp()
    decoded_password = generate_password(formatted_time)
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": mpesa_keys.businessShortCode,
        "Password": decoded_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerBuyGoodsOnline",
        "Amount": "4",
        "PartyA": mpesa_keys.phone_no,
        "PartyB": mpesa_keys.businessShortCode,
        "PhoneNumber": mpesa_keys.phone_no,
        "CallBackURL": "https://mark.com/lipanampesa/",
        "AccountReference": "32168434",
        "TransactionDesc": "Tithe"
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)


lipa_na_mpesa()
