from django.conf.urls.defaults import *
from django.contrib import admin
import os
from django.conf import settings
import calloway

admin.autodiscover()

handler500 = 'calloway.django_ext.views.custom_server_error'

sitemaps = {
}

urlpatterns = patterns('',*calloway.get_urls(settings.DEBUG,settings.INSTALLED_APPS))

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.path.dirname(__file__), 'media2')}),
    )
