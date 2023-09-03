"""
WSGI config for djangok8s project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

import pathlib
import dotenv
from django.core.wsgi import get_wsgi_application

CURRENT_DIR = pathlib.Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent
ENV_FILE_PATH = BASE_DIR / ".env"
print(ENV_FILE_PATH,type(ENV_FILE_PATH))
dotenv.read_dotenv(str(ENV_FILE_PATH))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangok8s.settings')

application = get_wsgi_application()
