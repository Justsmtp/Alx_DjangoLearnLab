"""
WSGI config for social_media_api project.
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

# Add your project directory to the sys.path
path = '/home/Justsmtp/Alx_DjangoLearnLab/social_media_api'
if path not in sys.path:
    sys.path.append(path)

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_media_api.settings')

application = get_wsgi_application()
