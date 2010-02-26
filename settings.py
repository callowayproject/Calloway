import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Webmaster', 'webmaster@washingtontimes.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'dev.db'             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1
APPEND_SLASH = True

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://127.0.0.1:8000/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = 'http://127.0.0.1:8000/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '3e3f)^l&&&izq3an(dc+g4-+ts%&b27%%rop)1nx_)9cl85qr8'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_ext.middleware.cookie.UsernameInCookieMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'ban.middleware.DenyMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'livevalidation', # keep me above admin
    'admin_tools.theming', # keep me above admin
    'admin_tools.menu', # keep me above admin
    'admin_tools.dashboard', # keep me above admin
    'django.contrib.admin',
    'django.contrib.flatpages',
    'django.contrib.humanize',
    'django.contrib.comments',
    'django.contrib.markup',
    'django.contrib.redirects',
    'django_ext',
    'django_memcached',
    'pagination',
    'django_extensions',
    
    'staff',
    'stories',
    'categories',
    'editor',
    'mptt',
    'mptt_comments',
    'positions',
    'news_sitemaps',
    'robots',
    #'django_openid',
    'livevalidation',
    'piston',
    'offensivecontent',
    #'ban',
    #'logjam',
    #'varnishapp',
    'frontendadmin',
    'synagg',
    'massmedia',
    'native_tags',
    'staticmediamgr',
    'typogrify',
    'offensivecontent',
    'versionedcache',
    'google_analytics',
    
    # These need to be at the bottom
    'tinymce',
    'tagging',
    'reversion',    
)

SOUTH_AUTO_FREEZE_APP = True

DJANGO_MEMCACHED_REQUIRE_STAFF = True

CACHE_BACKEND = 'versionedcache.backend://localhost:11211/'
#CACHE_BACKEND = 'locmem:///'

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'relative_urls': False,
    'plugins': "safari,paste,advimage,preview",
    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_toolbar_align' : "left",
    'theme_advanced_buttons1' : "formatselect,bold,italic,underline,separator,bullist,numlist,separator,undo,separator,link,unlink,separator,charmap,image,paste,pasteword,separator,code,preview",
    'theme_advanced_buttons2' : "",
    'theme_advanced_buttons3' : "",
    'theme_advanced_statusbar_location' : "bottom",
    'width': "600",
    'height': "600",
}

TINYMCE_ADMIN_FIELDS = {
    'stories.story': ('body',),
    'staff.staffmember': ('bio',),
    'flatpages.flatpage': ('content',),
}

REVERSION_MODELS = ('stories.story','flatpages.flatpage')

PUBLICATION_NAME = 'The Washington Times'

VARNISH_WATCHED_MODELS = ('stories.story','flatpages.flatpage')

VARNISH_MANAGEMENT_ADDRS = ()

NATIVE_TAGS = (
    'native_tags.contrib.generic_content',
)

STATIC_MEDIA_COPY_PATHS = (
    {'from': 'media', 'to': 'media2'},
)
STATIC_MEDIA_COMPRESS_CSS = True
STATIC_MEDIA_COMPRESS_JS = True
try:
    from local_settings import *
except ImportError:
    pass

VERSION = '0.1'
