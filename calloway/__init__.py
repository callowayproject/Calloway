__version_info__ = {
    'major': 0,
    'minor': 1,
    'micro': 2,
    'releaselevel': 'final',
    'serial': 1
}

def get_version():
    vers = ["%(major)i.%(minor)i" % __version_info__, ]

    if __version_info__['micro']:
        vers.append(".%(micro)i" % __version_info__)
    if __version_info__['releaselevel'] != 'final':
        vers.append('%(releaselevel)s%(serial)i' % __version_info__)
    return ''.join(vers)

__version__ = get_version()


def get_middleware(debug,apps):
    yield 'django.middleware.cache.UpdateCacheMiddleware'
    yield 'django.middleware.common.CommonMiddleware'
    yield 'django.contrib.sessions.middleware.SessionMiddleware'
    yield 'django_ext.middleware.cookie.UsernameInCookieMiddleware'
    yield 'django.contrib.auth.middleware.AuthenticationMiddleware'
    yield 'django.middleware.gzip.GZipMiddleware'
    yield 'django.middleware.http.ConditionalGetMiddleware'
    yield 'django.middleware.doc.XViewMiddleware'
    if debug and 'debug_toolbar' in apps:
        yield 'debug_toolbar.middleware.DebugToolbarMiddleware'
    yield 'django.contrib.redirects.middleware.RedirectFallbackMiddleware'
    yield 'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
    yield 'django.middleware.transaction.TransactionMiddleware'
    yield 'pagination.middleware.PaginationMiddleware'
    if 'ban' in apps:
        yield 'ban.middleware.DenyMiddleware'
    yield 'django.middleware.cache.FetchFromCacheMiddleware'

def get_apps(debug, packages=None):
    yield 'django.contrib.auth'
    yield 'django.contrib.contenttypes'
    yield 'django.contrib.sessions'
    yield 'django.contrib.sites'
    yield 'django.contrib.flatpages'
    yield 'django.contrib.humanize'
    yield 'django.contrib.comments'
    yield 'django.contrib.markup'
    yield 'django.contrib.redirects'
    
    # Calloway
    yield 'django_ext'
    yield 'django_memcached'
    yield 'pagination'
    yield 'django_extensions'
    yield 'versionedcache'
    yield 'reversion'
    yield 'frontendadmin'

    lookup = {
        'media':['massmedia','staticmediamgr'],
        'admin':['admin_tools','admin_tools.theming','admin_tools.menu','admin_tools.dashboard','django.contrib.admin'],
        'comments':['mptt','mptt_comments','offensivecontent'],
        'staff':['staff'],
        'stories':['pullquote','stories'],
        'blogs':['viewpoint'],
        'categories':['categories','editor'],
        'polls':['pollit'],
        'tagging':['tagging'],
        'api':['piston'],
        'utils':['livevalidation','debug_toolbar','news_sitemaps','robots','ban','native_tags','google_analytics','hiermenu','synagg','uni_form','critic','mailfriend'],
        'registration':['registration','custom_registration'],
        'tinymce':['tinymce'],
    }
    
    if packages is None:
        packages = lookup.keys()

    for package in ('media','admin','comments','staff','stories','blogs','categories','polls','tagging','api','utils','tinymce'):
        for app in lookup[package]:
            yield app
        if package == 'blogs' and ('stories' in packages or 'blogs' in packages):
            yield 'positions'

def get_urls(debug,apps):
    from django.conf.urls.defaults import *
    
    yield (r'^cache/', include('django_memcached.urls'))
    yield (r'^admin/log/', include('logjam.urls'))
    yield (r'^admin/varnish/', include('varnishapp.urls'))
    yield (r'^admin_tools/', include('admin_tools.urls'))
    yield (r'^frontendadmin/', include('frontendadmin.urls'))
    yield (r'^registration/', include('registration.backends.default.urls'))
    yield (r'^accounts/', include('registration.urls'))
    yield (r'^profile/', include('profiles.urls'))
    yield url(r'^robots.txt', 'robots.views.rules_list', name='robots_rule_list')
    
    if 'stories' in apps or 'blogs' in apps:
        yield (r'^position_management/', include('positions.urls'))
    if 'critic' in apps:
        yield (r'^critic/', include('critic.urls'))
    if 'api' in apps:
        yield (r'^api/', include('api.urls'))
    if 'synagg' in apps:
        yield (r'^syn/', include('synagg.urls'))
    if 'massmedia' in apps:
        yield (r'^multimedia/', include('massmedia.urls'))
    if 'news_sitemaps' in apps:
        yield (r'^sitemaps/', include('news_sitemaps.urls'))
    if 'stories' in apps:
        yield (r'^news/', include('stories.urls'))
    if 'mailfriend' in apps:
        yield (r'^mail-a-friend/', include('mailfriend.urls'))
    if 'categories' in apps:
        yield (r'^categories/', include('categories.urls'))
    if 'offensivecontent' in apps:
        yield (r'^moderator/', include('offensivecontent.urls'))
    if 'pollit' in apps:
        yield (r'^polls/', include('pollit.urls'))
    if 'staff' in apps:
        yield (r'^staff/', include('staff.urls'))
    if 'blogs' in apps:
        yield (r'^blog/', include('viewpoint.urls'))
    yield (r'^$', 'django.views.generic.simple.direct_to_template', {'template':'homepage.html'})


#def configure(debug,*a):
#    apps = get_apps(debug,*a)
#    return apps,get_middleware(debug, apps),get_