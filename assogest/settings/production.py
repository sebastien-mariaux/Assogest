import os
from .base import *

# Debug temporaire
print("Database connection parameters:")
print(f"NAME: {os.getenv('DB_NAME')}")
print(f"USER: {os.getenv('DB_USER')}")
print(f"PASSWORD: {'*' * len(os.getenv('DB_PASSWORD', ''))}")
print(f"HOST: {os.getenv('DB_HOST')}")
print(f"PORT: {os.getenv('DB_PORT')}")

DEBUG = False
ALLOWED_HOSTS = [os.getenv('DOMAIN_NAME')]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'db'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# Sécurité supplémentaire pour la production
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
