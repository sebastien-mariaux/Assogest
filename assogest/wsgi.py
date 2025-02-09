"""
WSGI config for assogest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Utilise local par défaut, peut être surchargé par l'environnement
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assogest.settings.local')

application = get_wsgi_application()
