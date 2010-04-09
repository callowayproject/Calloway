from django.conf.urls.defaults import *
from django.contrib import admin
import os
from django.conf import settings

admin.autodiscover()

handler500 = 'calloway.django_ext.views.custom_server_error'

sitemaps = {
}

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
)
from calloway.urls import urlpatterns as calloway_patterns

urlpatterns += calloway_patterns

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.path.dirname(__file__), 'media2')}),
    )
