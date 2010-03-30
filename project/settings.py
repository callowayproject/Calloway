# Django settings for project project.

import bombay
import os
import sys

BOMBAY_ROOT = os.path.abspath(os.path.dirname(bombay.__file__))
sys.path.insert(0, os.path.join(BOMBAY_ROOT, 'apps'))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

from bombay.settings import *

ADMINS = (
    ('$$$$NAME$$$$', '$$$$EMAIL_ADDRESS$$$$'),
)
MANAGERS = ADMINS

SECRET_KEY = '$$$$SECRET_KEY$$$$'

DATABASE_ENGINE = 'sqlite3'    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'dev.db'       # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
USE_I18N = True

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_ROOT = os.path.join(STATIC_ROOT, 'ugc')
MEDIA_URL = '/media/ugc/'
STATIC_URL = '/media/'

AUTH_PROFILE_MODULE = ''

PUBLICATION_NAME = 'The Effington Times'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
) + BOMBAY_TEMPLATE_DIRS

CACHE_BACKEND = 'versionedcache.backend://localhost:11211/'

STATIC_MEDIA_COPY_PATHS = (
    {'from': os.path.join(BOMBAY_ROOT, 'media'), 'to': 'media2'},
    {'from': 'media', 'to': 'media2'},
)

STATIC_MEDIA_COMPRESS_CSS = True
STATIC_MEDIA_COMPRESS_JS = True

INSTALLED_APPS = APPS_CORE + \
    APPS_ADMIN + \
    APPS_STAFF + \
    APPS_REVERSION + \
    APPS_STORIES + \
    APPS_BOMBAY_DEFAULT + \
    APPS_MPTT + \
    APPS_CATEGORIES + \
    APPS_COMMENT_UTILS + \
    APPS_FRONTEND_ADMIN + \
    APPS_MEDIA + \
    APPS_UTILS + \
    APPS_REGISTRATION + \
    APPS_TINYMCE 


try:
    from local_settings import *
except ImportError:
    pass

VERSION = '0.1'