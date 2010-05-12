import os
import sys

CALLOWAY_ROOT = os.path.abspath(os.path.dirname(__file__))

SITE_ID = 1
APPEND_SLASH = True

MEDIA_URL = 'http://127.0.0.1:8000/media/'
STATIC_URL = MEDIA_URL
ADMIN_MEDIA_PREFIX = '/admin-media/'

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
    'staticmediamgr.context_processor.static_url',
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
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'ban.middleware.DenyMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django_ext.caseinsensitiveauth.CaseInsensitiveModelBackend',
    'django.contrib.auth.backends.ModelBackend',
)


ROOT_URLCONF = 'urls'

CALLOWAY_TEMPLATE_DIRS = (
    os.path.join(CALLOWAY_ROOT, 'templates'),
)

APPS_CORE = ( # Suggested: APPS_TINYMCE, APPS_REVERSION (for flatpages)
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.humanize',
    'django.contrib.comments',
    'django.contrib.markup',
    'django.contrib.redirects',
)
APPS_ADMIN = (
    'massmedia',
    'livevalidation', # keep me above admin
    'admin_tools', # for the media copying
    'admin_tools.theming', # keep me above admin
    'admin_tools.menu', # keep me above admin
    'admin_tools.dashboard', # keep me above admin
    'django.contrib.admin',
)
APPS_CALLOWAY_DEFAULT = (
    'django_ext',
    'django_memcached',
    'pagination',
    'django_extensions',
    'versionedcache',
)
APPS_MPTT = ('mptt',)

APPS_STAFF = ('staff',) # Suggested: APPS_TINYMCE

APPS_REVERSION = (
    'reversion',
)

APPS_STORIES = ( # Suggested: APPS_TINYMCE, APPS_REVERSION
    'stories',
    'positions',
    'news_sitemaps',
    'viewpoint',
    'pullquote',
)
APPS_CATEGORIES = ( # Requires APPS_MPTT
    'categories',
    'editor',
)
APPS_COMMENT_UTILS = ( # Requires APPS_MPTT
    'mptt_comments',
    'offensivecontent',
    'pollit',
)
APPS_FRONTEND_ADMIN = (
    'livevalidation',
    'frontendadmin',
)
APPS_MEDIA = (
    'tagging',
)
APPS_UTILS = (
    'robots',
    'piston',
    'ban',
    'native_tags',
    'staticmediamgr',
    'typogrify',
    'google_analytics',
    'hiermenu',
    'synagg',
    'uni_form',
    'critic',
    'mailfriend',
    'debug_toolbar',
)
APPS_REGISTRATION = (
    'registration',
    'custom_registration',
)
APPS_TINYMCE = (
    'tinymce',
)
DJANGO_MEMCACHED_REQUIRE_STAFF = True

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'relative_urls': False,
    'plugins': "safari,paste,advimage,advlink,preview,fullscreen,media,searchreplace",
    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_toolbar_align' : "left",
    'theme_advanced_buttons1' : "bold,italic,underline,strikethrough,blockquote,|,bullist,numlist,|,link,unlink,|,charmap,image,media,pastetext,pasteword,search,replace,|,code,fullscreen,preview",
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

VARNISH_WATCHED_MODELS = ('stories.story','flatpages.flatpage')

VARNISH_MANAGEMENT_ADDRS = ()

NATIVE_TAGS = (
    'native_tags.contrib.generic_content',
)

ADMIN_TOOLS_MENU = 'calloway.menu.CustomMenu'

STORY_RELATION_MODELS = ['massmedia.audio', 'massmedia.image', 'massmedia.document',
    'massmedia.video', 'massmedia.collection', 'stories.story','viewpoint.entry','viewpoint.blog','pollit.poll',]

CATEGORIES_RELATION_MODELS = ['pollit.poll',]

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)
