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

        "ConfirmationURL": mpesa_keys.mpesa_c2b_confirmation_url,
        "ValidationURL": mpesa_keys.mpesa_c2b_validation_url}

    try:
        response = requests.post(api_url, json=request, headers=headers)
    except:
        response = requests.post(api_url, json=request, headers=headers, verify=False)
    print(response.text)


# register_url()


def simulate_c2b_transaction(amount, bill_ref_number, msisdn):
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "ShortCode": mpesa_keys.shortcode,
        "CommandID": "CustomerPayBillOnline",
        "Amount": str(amount),
        "Msisdn": str(msisdn),
        "BillRefNumber": str(bill_ref_number)}
    try:
        response = requests.post(api_url, json=request, headers=headers)
    except:
        response = requests.post(api_url, json=request, headers=headers, verify=False)

    print(response.text)


simulate_c2b_transaction(20.0, 'noma', mpesa_keys.test_msisdn)
