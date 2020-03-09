import requests
import mpesa_keys
from access_token import generate_access_token


def register_url():
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "ShortCode": mpesa_keys.shortcode,
        "ResponseType": "Completed",
        # This is what will happen incase safaricom sends you a response of your transaction and your server is not online. Options Canceled or Completed
        "ConfirmationURL": "https://pacific-castle-77566.herokuapp.com/api/payments/c2b_confirmation/",
        "ValidationURL": "https://pacific-castle-77566.herokuapp.com/api/payments/c2b_validation"}

    try:
        response = requests.post(api_url, json=request, headers=headers)
    except:
        response = requests.post(api_url, json=request, headers=headers, verify=False)
    print(response.text)


#register_url()


def simulate_c2b_transaction():
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "ShortCode": mpesa_keys.shortcode,
        "CommandID": "CustomerPayBillOnline",
        "Amount": "2",
        "Msisdn": mpesa_keys.test_msisdn,
        "BillRefNumber": "1234567"}

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

# simulate_c2b_transaction()
