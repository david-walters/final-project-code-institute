"""
WSGI config for cass_galaar project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cass_galaar.settings')

application = get_wsgi_application()

# Run database population script
from django.core.management import call_command
try:
    call_command('populate_perfume')
except Exception as e:
    print(f"Error populating perfume data: {e}")