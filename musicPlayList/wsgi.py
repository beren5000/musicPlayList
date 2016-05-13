"""
WSGI config for musicPlayList project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

try:
    from rol import settings_name
except ImportError:
    settings_name = "settings"

settings_var = "musicPlayList."+settings_name
print settings_var

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_var)

application = get_wsgi_application()
