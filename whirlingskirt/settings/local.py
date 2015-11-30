# settings/local.py
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wpg+&013q9d5y&+@+61(9=0#$28w(lz0n#d3j#ttxde!omsa-7'

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'skirt',
        'USER': 'explorer',
        'PASSWORD': 'explorer',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}