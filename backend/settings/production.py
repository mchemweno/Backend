"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# For gmail
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ku72ry8an2aq5(8l4b+di1!jvp7u)6&1obl-4-(h#)-qe7&#xx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['pacific-castle-77566.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'professionals_app.apps.ProffesionalsAppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'rest_framework',
    'djoser',
    'imagekit',
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd9k17lpehvouvv',
        'USER': 'akqzrzftedrxig',
        'PASSWORD': '14a110801162e9adb0cf6cbf06d39c9c6f5794a6d77264847f75021ce47f6b15',
        'HOST': 'ec2-3-229-210-93.compute-1.amazonaws.com',
        'PORT': '5432'
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSIONS_CLASSES': (
        'rest_framework.permissions.IsAuthenticated'
    )
}

AUTH_USER_MODEL = 'professionals_app.User'

DJOSER = {
    'USER_ID_FIELD': 'email',
    'LOGIN_FIELD': 'email',
    'PASSWORD_RESET_CONFIRM_URL': 'professionals_app/users/password-reset/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'ACTIVATION_URL': 'professionals_app/users/activate/{uid}/{token}',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'LOGOUT_ON_PASSWORD_CHANGE': True,
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,
    'SERIALIZERS': {
        'user_create': 'professionals_app.serializers.UserCreateSerializer',
        'user': 'professionals_app.serializers.UserCreateSerializer',
        'activation': 'djoser.serializers.ActivationSerializer',
        'password_reset': 'djoser.serializers.SendEmailResetSerializer',
        'password_reset_confirm': 'djoser.serializers.PasswordResetConfirmSerializer',
        'password_reset_confirm_retype': 'djoser.serializers.PasswordResetConfirmRetypeSerializer',
        'set_password': 'djoser.serializers.SetPasswordSerializer',
        'set_password_retype': 'djoser.serializers.SetPasswordRetypeSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    },
    'EMAIL': {
        'activation': 'djoser.email.ActivationEmail'
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

AWS_ACCESS_KEY_ID = "AKIAROBCEZHY6NZFZZB3"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = "professionals-backend"

# AWS Config
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_REGION_NAME = 'eu-west-2'
AWS_S3_SIGNATURE_VERSION = 's3v4'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
