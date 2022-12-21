"""
WSGI config for ymgallery_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

setting_module = 'ymgallery_backend.settings.pro' if 'WEBSITE_HOSTNAME' in os.environ else 'ymgallery_backend.settings.local'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', setting_module)

application = get_wsgi_application()
