from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

handler500 = 'bombay.django_ext.views.custom_server_error'

sitemaps = {
}

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
)
from bombay.urls import urlpatterns as bombay_patterns

urlpatterns += bombay_patterns