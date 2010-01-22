from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps import FlatPageSitemap

admin.autodiscover()

from news_sitemaps import NewsSitemap
from stories.models import Story

class StorySitemap(NewsSitemap):
    def items(self):
        return Story.published.all()
        
    def lastmod(self, obj):
        return obj.publish_date
    
sitemaps = {
    'flatpages': FlatPageSitemap,
    'stories': StorySitemap    
}

urlpatterns = patterns('',
    (r'^cache/', include('django_memcached.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^api/', include('api.urls')),
    (r'^news/', include('stories.urls')),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.index', {'sitemaps': sitemaps}),
    (r'^sitemap-stories\.xml', 'news_sitemaps.views.news_sitemap', {'sitemaps': {'stories': sitemaps['stories']}}),    
    (r'^sitemap-(?P<section>.+)\.xml', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),    
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'^media/(?P<path>.*)$', 'serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
