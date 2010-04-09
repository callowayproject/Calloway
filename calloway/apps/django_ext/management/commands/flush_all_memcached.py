from django.core.management.base import NoArgsCommand
from django.db import transaction
from django.conf import settings

class Command(NoArgsCommand):
    help = "Flushes memcached"

    def handle_noargs(self, **options):
        try:
            import memcache
        except ImportError:
            return
        if 'memcached' in settings.CACHE_BACKEND:
            servers = settings.CACHE_BACKEND.replace('memcached://',
                '').replace('/','').split(';')
            mc = memcache.Client(servers, debug=0)
            mc.flush_all()