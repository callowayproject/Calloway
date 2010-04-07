from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    (r'^cache/', include('django_memcached.urls')),
    (r'^admin/log/', include('logjam.urls')),
    (r'^admin/varnish/', include('varnishapp.urls')),
    (r'^position_management/', include('positions.urls')),
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
    (r'^blog/', include('viewpoint.urls')),
    (r'^admin_tools/', include('admin_tools.urls')),
    url(r'^robots.txt', 'robots.views.rules_list', name='robots_rule_list'),
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template':'homepage.html'}),    
)
