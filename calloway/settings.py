import os
import sys
import django
django_version = django.VERSION
from django.conf import settings

CALLOWAY_ROOT = os.path.abspath(os.path.dirname(__file__))

#from calloway.default_settings import SITE_ID, APPEND_SLASH, MEDIA_URL, \
from default_settings import *

class DynamicList(list):
    """Allows for the dynamic list created based on a base set of items, the
    django version and what apps are installed"""
    DEFAULT_ITEMS = []
    DJANGO_VERS_MAPPING = {
        0: [],
        1: [],
        2: [],
        3: []
    }
    APP_MAPPING = {
    }
    
    def __init__(self, *args):
        if len(args) > 1:
            self.DEFAULT_ITEMS = args[:]
        elif args and isinstance(args[0], basestring):
            self.DEFAULT_ITEMS = [args[0],]
        elif args:
            self.DEFAULT_ITEMS = args[0]
        self.data = None
    
    def _build_list(self):
        from django.conf import settings 
        INSTALLED_APPS = settings.INSTALLED_APPS[:]
        from django import VERSION
        
        items = self.DEFAULT_ITEMS[:]
        items.extend(self.DJANGO_VERS_MAPPING[VERSION[1]])
        
        for app, val in self.APP_MAPPING.items():
            if app in INSTALLED_APPS:
                items.extend(val)
        self.data = items
    
    def __len__(self):
        if self.data is None:
            self._build_list()
        return len(self.data)
    
    def __getitem__(self, key):
        if self.data is None:
            self._build_list()
        return self.data[key]
    
    def __iter__(self):
        if self.data is None:
            self._build_list()
        return self.data.__iter__()
    
    def __contains__(self, item):
        if self.data is None:
            self._build_list()
        return self.data.__contains__(item)
    
    def __repr__(self):
        if self.data is None:
            self._build_list()
        return self.data.__repr__()

class TemplateContextProcs(DynamicList):
    DEFAULT_ITEMS = [
        'django.core.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.request',
    ]
    APP_MAPPING = {
        'staticmediamgr': ['staticmediamgr.context_processor.static_url',],
    }

TEMPLATE_CONTEXT_PROCESSORS = TemplateContextProcs()

class AuthenticationBackends(DynamicList):
    DEFAULT_ITEMS = [
        'django.contrib.auth.backends.ModelBackend',
    ]
    APP_MAPPING = {
        'django_ext': ['django_ext.caseinsensitiveauth.CaseInsensitiveModelBackend',]
    }

AUTHENTICATION_BACKENDS = AuthenticationBackends()

class Middleware(DynamicList):
    """
    Since the placement of the middleware class is important, and the predecessor
    and successor are or can be unknown we are using a tuple consisting of a rank
    and value.
    
    The default classes are each ranked in multiples of 10. This allows plenty 
    room for other apps to insert their class(es) between them.
    
    The DJANGO_VER_MAPPING looks at the minor version number of Django to 
    dynamically insert version-specific middleware classes.
    
    Each application in the APP_MAPPING dictionary has a value that is a list
    of rank-class tuples that can extend the DEFAULT_CLASSES list.
    """
    # Maps the minor version number of Django (1.0, 1.1, 1.2)
    DJANGO_VERS_MAPPING = {
        0 : [],
        1 : [],
        2 : [
            (34, 'django.middleware.csrf.CsrfViewMiddleware',),
            (44, 'django.contrib.messages.middleware.MessageMiddleware',),
            (64, 'django.middleware.csrf.CsrfResponseMiddleware',),
        ]
    }
    
    APP_MAPPING = {
        'django_ext': [(36, 'django_ext.middleware.cookie.UsernameInCookieMiddleware',)],
        'debug_toolbar': [(75, 'debug_toolbar.middleware.DebugToolbarMiddleware',)],
        'pagination': [(103, 'pagination.middleware.PaginationMiddleware',)],
        'ban': [(106, 'ban.middleware.DenyMiddleware',)],
    }
    
    DEFAULT_ITEMS = [
        (10, 'django.middleware.cache.UpdateCacheMiddleware',),
        (20, 'django.middleware.common.CommonMiddleware',),
        (30, 'django.contrib.sessions.middleware.SessionMiddleware',),
        (40, 'django.contrib.auth.middleware.AuthenticationMiddleware',),
        (50, 'django.middleware.gzip.GZipMiddleware',),
        (60, 'django.middleware.http.ConditionalGetMiddleware',),
        (70, 'django.middleware.doc.XViewMiddleware',),
        (80, 'django.contrib.redirects.middleware.RedirectFallbackMiddleware',),
        (90, 'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',),
        (100, 'django.middleware.transaction.TransactionMiddleware',),
        (110, 'django.middleware.cache.FetchFromCacheMiddleware',),
    ]
    
    def _build_list(self):
        super(Middleware, self)._build_list()
        self.data.sort(cmp=lambda x,y: cmp(x[0], y[0]))
        self.data = [x[1] for x in self.data]

MIDDLEWARE_CLASSES = Middleware()

__all__ = [
    'SITE_ID', 'APPEND_SLASH', 'MEDIA_URL', 'STATIC_URL', 'ADMIN_MEDIA_PREFIX',
    'TEMPLATE_LOADERS', 'ROOT_URLCONF', 'CALLOWAY_TEMPLATE_DIRS', 'APPS_CORE',
    'APPS_ADMIN','APPS_CALLOWAY_DEFAULT','APPS_CACHING','APPS_MPTT','APPS_STAFF',
    'APPS_REVERSION','APPS_STORIES','APPS_CATEGORIES','APPS_COMMENT_UTILS',
    'APPS_FRONTEND_ADMIN','APPS_MEDIA','APPS_UTILS','APPS_REGISTRATION',
    'APPS_TINYMCE','DJANGO_MEMCACHED_REQUIRE_STAFF','TINYMCE_DEFAULT_CONFIG',
    'TINYMCE_ADMIN_FIELDS','REVERSION_MODELS','VARNISH_WATCHED_MODELS',
    'VARNISH_MANAGEMENT_ADDRS','NATIVE_TAGS','ADMIN_TOOLS_MENU',
    'CATEGORIES_RELATION_MODELS','INTERNAL_IPS',
    'STATIC_MEDIA_PURGE_OLD_FILES','DEBUG_TOOLBAR_PANELS','DEBUG_TOOLBAR_CONFIG',
    'MIDDLEWARE_CLASSES','TEMPLATE_CONTEXT_PROCESSORS', 'AUTHENTICATION_BACKENDS'
    ]
