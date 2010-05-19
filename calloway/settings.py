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

AUTHENTICATION_BACKENDS = (
    'django_ext.caseinsensitiveauth.CaseInsensitiveModelBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'urls'

CALLOWAY_TEMPLATE_DIRS = (
    os.path.join(CALLOWAY_ROOT, 'templates'),
)

DJANGO_MEMCACHED_REQUIRE_STAFF = True

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'relative_urls': False,
    'plugins': "safari,paste,advimage,advlink,preview,fullscreen,searchreplace",
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

VARNISH_MANAGEMENT_ADDRS = ('localhost:61',)

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
