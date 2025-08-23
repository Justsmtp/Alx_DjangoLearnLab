"""
WSGI config for social_media_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

"""
WSGI config for social_media_api project on PythonAnywhere.
"""

import os
import sys

# Add project root to Python path
project_home = '/home/justsmtp/Django_Framework/social_media_api'
if project_home not in sys.path:
    sys.path.append(project_home)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_media_api.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
