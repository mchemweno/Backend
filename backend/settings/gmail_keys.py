import os

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('email')
EMAIL_HOST_PASSWORD = os.environ.get('password')
EMAIL_PORT = 587