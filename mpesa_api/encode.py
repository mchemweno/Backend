import base64
import mpesa_keys


def generate_password(formatted_time):
    data_to_encode = mpesa_keys.businessShortCode + mpesa_keys.lipa_na_mpesa_passkey + formatted_time
    encoded_string = base64.b64encode(data_to_encode.encode())

    decoded_password = encoded_string.decode('utf-8')
    return decoded_password
