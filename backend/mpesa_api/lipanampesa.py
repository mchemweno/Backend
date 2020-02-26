import requests
import base64
import mpesa_keys
from datetime import datetime
from requests.auth import HTTPBasicAuth

unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")

data_to_encode = mpesa_keys.businessShortCode + mpesa_keys.lipa_na_mpesa_passkey + formatted_time
encoded_string = base64.b64encode(data_to_encode.encode())

decoded_password = encoded_string.decode('utf-8')

consumer_key = mpesa_keys.consumer_key
consumer_secret = mpesa_keys.consumer_secret
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

print(r.json())

json_response = r.json()

my_access_token = json_response['access_token']


def lipa_na_mpesa():
    access_token = my_access_token
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
