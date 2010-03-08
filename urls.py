from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

handler500 = 'django_ext.views.custom_server_error'

sitemaps = {
}

urlpatterns = patterns('',
    (r'^cache/', include('django_memcached.urls')),
    (r'^admin/log/', include('logjam.urls')),
    (r'^admin/varnish/', include('varnishapp.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^api/', include('api.urls')),
    (r'^syn/', include('synagg.urls')),
    (r'^massmedia/', include('massmedia.urls')),
    (r'^sitemaps/', include('news_sitemaps.urls')),
    (r'^news/', include('stories.urls')),
    (r'^categories/', include('categories.urls')),
    (r'^frontendadmin/', include('frontendadmin.urls')),
    (r'^registration/', include('custom_registration.backends.email.urls')),
    (r'^accounts/', include('registration.urls')),
    (r'^profile/', include('profiles.urls')),
    url(r'^robots.txt', 'robots.views.rules_list', name='robots_rule_list'),
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template':'homepage.html'}),    
)

import os
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.path.dirname(__file__), 'media2')}),
    )
