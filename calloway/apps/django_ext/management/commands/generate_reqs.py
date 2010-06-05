from django.core.management.base import NoArgsCommand
from django.db import transaction
from django.conf import settings
import os

mapping = {
    'admin_tools': ('django-admin-tools==0.2',),
    'admin_tools.dashboard': ('django-admin-tools==0.2',),
    'admin_tools.menu': ('django-admin-tools==0.2',),
    'admin_tools.theming': ('django-admin-tools==0.2',),
    'ban': ('django-ban==0.1', 'ipcalc>=0.1', ),
    'categories': ('django-categories==0.4.3','django-mptt-2==0.3', ),
    'critic': ('critic==0.1.1',),
    'debug_toolbar': ('django-debug-toolbar==0.8.3',),
    'django_extensions': ('django-extensions==0.4.1',),
    'django_memcached': ('django-memcached==0.1.2', 'python-memcached==1.44',),
    'editor': ('django-categories==0.4.3','django-mptt-2==0.3', ),
    'frontendadmin': ('django-frontendadmin==0.4', 'django-livevalidation==0.1.1',),
    'google_analytics': ('google_analytics==0.2',),
    'hiermenu': ('hiermenu==0.1',),
    'livevalidation': ('django-livevalidation==0.1.1',),
    'mailfriend': ('django-mailfriend==1.0',),
    'massmedia': ('massmedia==0.5.1', 'django-tagging==0.3.1', 'IPTCInfo', 'hachoir-metadata', 'hachoir-core', 'hachoir-parser',),
    'mptt': ('django-mptt-2==0.3',),
    'mptt_comments': ('django-mptt-comments==0.1.1','django-mptt-2==0.3',),
    'native_tags': ('django-native-tags==0.4',),
    'news_sitemaps': ('django-news-sitemaps==0.1.2',),
    'offensivecontent': ('offensivecontent==0.2.6',),
    'pagination': ('django-pagination==1.0.8',),
    'piston': ('django-piston==0.2.2',),
    'pollit': ('pollit==0.1.1',),
    'positions': ('kamasutra==0.1.5',),
    'pullquote': ('pullquote==0.1.1',),
    'registration': ('django-registration==0.8-alpha-1',),
    'reversion': ('django-reversion==1.2.1',),
    'robots': ('django-robots==0.7.0',),
    'staff': ('django-staff==0.3.2',),
    'staticmediamgr': ('django-staticmediamgr==0.5.3',),
    'stories': ('django-stories==0.3.6', 'BeautifulSoup', 'pytidylib'),
    'synagg': ('django-synagg', 'feedparser==4.1',),
    'tagging': ('django-tagging==0.3.1',),
    'tinymce': ('django-tinymce==1.5.1beta1',),
    'uni_form': ('django-uni-form==0.7',),
    'versionedcache': ('versionedcache==0.1.0dev',),
    'viewpoint': ('viewpoint==0.6.2',),
}

not_included = {
    'memcache_status': ('django-memcache-status==1.0.1',),
    'varnishapp': ('django-varnish==0.1', 'python-varnish==0.1',),
    'haystack': ('django-haystack==1.0.1-final',),
}
unknown = {
    'python-dateutil': 'python-dateutil==1.4.1',
    'django-logjam': 'django-logjam==0.1.1',
    'django-picklefield': 'django-picklefield==0.1',
    'django-profiles': 'django-profiles>=0.2',
    'simplejson': 'simplejson==2.0.9',
    'lxml':'lxml',
}


class Command(NoArgsCommand):
    help = "Prints out a requirements file"

    def handle_noargs(self, **options):
        # try:
        #     reqs = open(os.path.join(settings.CALLOWAY_ROOT, 'requirements.txt')).read()
        # except IOError, e:
        #     print "Returned an error reading the requirements file: %s" % e
        # 
        # print reqs
        from django.conf import settings
        reqs = set()
        
        for app in settings.INSTALLED_APPS:
            if app in mapping.keys():
                reqs |= set(mapping[app])
        print "--extra-index-url=http://opensource.washingtontimes.com/pypi/simple/"
        for item in reqs:
            print item
