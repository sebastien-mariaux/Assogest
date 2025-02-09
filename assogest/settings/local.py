from .base import *

DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django',
        'USER': 'postgres',
        'PASSWORD': 'django123',
        'HOST': 'localhost',
        'PORT': 5434,
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@vmh_1+ilm0fa#ab4a5yp7!h0%uf3sg_(g!4z3)qjxc&c+hly='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Configuration du mode développement
if DEBUG:
    INTERNAL_IPS = [
        "127.0.0.1",
    ]