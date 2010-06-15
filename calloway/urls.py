from django.conf.urls.defaults import patterns, url, include
from django.conf import settings

url_mapping = {
    'django_memcached': (r'^cache/', include('django_memcached.urls')),
    'logjam': (r'^admin/log/', include('logjam.urls')),
    'varnishapp': (r'^admin/varnish/', include('varnishapp.urls')),
    'positions': (r'^admin/position_management/', include('positions.urls')),
    'critic': (r'^critic/', include('critic.urls')),
    'api': (r'^api/', include('api.urls')),
    'synagg': (r'^syn/', include('synagg.urls')),
    'massmedia': (r'^multimedia/', include('massmedia.urls')),
    'news_sitemaps': (r'^sitemaps/', include('news_sitemaps.urls')),
    'stories': (r'^news/', include('stories.urls')),
    'mailfriend': (r'^mail-a-friend/', include('mailfriend.urls')),
    'categories': (r'^categories/', include('categories.urls')),
    'frontentadmin': (r'^frontendadmin/', include('frontendadmin.urls')),
    'offensivecontent': (r'^moderator/', include('offensivecontent.urls')),
    'profiles': (r'^profile/', include('profiles.urls')),
    'pollit': (r'^polls/', include('pollit.urls')),
    'staff': (r'^staff/', include('staff.urls')),
    'viewpoint': (r'^blog/', include('viewpoint.urls')),
    'admin_tools': (r'^admin_tools/', include('admin_tools.urls')),
    'robots': url(r'^robots.txt', 'robots.views.rules_list', name='robots_rule_list'),
}
otherpatterns = [url_mapping[app] for app in settings.INSTALLED_APPS if app in url_mapping]

if 'registration' in settings.INSTALLED_APPS:
    otherpatterns.append((r'^registration/', include('registration.backends.default.urls')))
    otherpatterns.append((r'^accounts/', include('registration.urls')))

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template':'homepage.html'}),    
    *otherpatterns
)


# urlpatterns = patterns('',
#     (r'^cache/', include('django_memcached.urls')),
#     (r'^admin/log/', include('logjam.urls')),
#     (r'^admin/varnish/', include('varnishapp.urls')),
#     (r'^admin/position_management/', include('positions.urls')),
#     (r'^critic/', include('critic.urls')),
#     (r'^api/', include('api.urls')),
#     (r'^syn/', include('synagg.urls')),
#     (r'^multimedia/', include('massmedia.urls')),
#     (r'^sitemaps/', include('news_sitemaps.urls')),
#     (r'^news/', include('stories.urls')),
#     (r'^mail-a-friend/', include('mailfriend.urls')),
#     (r'^categories/', include('categories.urls')),
#     (r'^frontendadmin/', include('frontendadmin.urls')),
#     (r'^registration/', include('registration.backends.default.urls')),
#     (r'^accounts/', include('registration.urls')),
#     (r'^moderator/', include('offensivecontent.urls')),
#     (r'^profile/', include('profiles.urls')),
#     (r'^polls/', include('pollit.urls')),
#     (r'^staff/', include('staff.urls')),
#     (r'^blog/', include('viewpoint.urls')),
#     (r'^admin_tools/', include('admin_tools.urls')),
#     url(r'^robots.txt', 'robots.views.rules_list', name='robots_rule_list'),
#     (r'^$', 'django.views.generic.simple.direct_to_template', {'template':'homepage.html'}),    
# )
