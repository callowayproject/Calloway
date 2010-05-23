#!/usr/bin/env python

import os
import sys
import re
from random import choice
from subprocess import Popen, call, PIPE


HAS_VENV = bool(Popen(['which','virtualenv'], stdout=PIPE).communicate()[0])
if not HAS_VENV:
    print "virtualenv is required to run this script. Please install it with\n  easy_install virtualenv\n\nor\n\n  pip virtualenv"
    sys.exit(1)

HAS_VENVW = bool(Popen(['which','virtualenvwrapper_bashrc'], stdout=PIPE).communicate()[0])
if not HAS_VENVW:
    print "virtualenvwrapper is required to run this script. Please install it with\n  easy_install virtualenvwrapper\n\nor\n\n  pip virtualenvwrapper"
    sys.exit(1)

CHARS = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
BLACKLIST = (
    'jquery',
    '.tar.gz',
    'admin/css',
    'admin/img',
    'admin/js',
    '/.git/',
    '.svn',
    '.hg',
)

email_re = re.compile(
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"' # quoted-string
    r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', re.IGNORECASE)  # domain

def format(func):
    def inner(*a):
        return ''.join(('\t%s,\n' % _ for _ in func(*a)))
    return inner

@format
def get_middleware(apps):
    yield "'django.middleware.cache.UpdateCacheMiddleware'"
    yield "'django.middleware.common.CommonMiddleware'"
    yield "'django.contrib.sessions.middleware.SessionMiddleware'"
    yield "'django_ext.middleware.cookie.UsernameInCookieMiddleware'"
    yield "'django.contrib.auth.middleware.AuthenticationMiddleware'"
    yield "'django.middleware.gzip.GZipMiddleware'"
    yield "'django.middleware.http.ConditionalGetMiddleware'"
    yield "'django.middleware.doc.XViewMiddleware'"
    if 'debug_toolbar' in apps:
        yield "'debug_toolbar.middleware.DebugToolbarMiddleware'"
    yield "'django.contrib.redirects.middleware.RedirectFallbackMiddleware'"
    yield "'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'"
    yield "'django.middleware.transaction.TransactionMiddleware'"
    yield "'pagination.middleware.PaginationMiddleware'"
    if 'ban' in apps:
        yield "'ban.middleware.DenyMiddleware'"
    yield "'django.middleware.cache.FetchFromCacheMiddleware'"
    
@format
def get_apps(packages=None):
    yield "'django.contrib.auth'"
    yield "'django.contrib.contenttypes'"
    yield "'django.contrib.sessions'"
    yield "'django.contrib.sites'"
    yield "'django.contrib.flatpages'"
    yield "'django.contrib.humanize'"
    yield "'django.contrib.comments'"
    yield "'django.contrib.markup'"
    yield "'django.contrib.redirects'"
    
    # Calloway
    yield "'django_ext'"
    yield "'django_memcached'"
    yield "'pagination'"
    yield "'django_extensions'"
    yield "'versionedcache'"
    yield "'reversion'"
    yield "'frontendadmin'"

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
        'utils':['livevalidation','news_sitemaps','robots','ban','native_tags','google_analytics','hiermenu','synagg','uni_form','critic','mailfriend'],
        'registration':['registration','custom_registration'],
        'debug':['debug_toolbar'],
        'tinymce':['tinymce'],
    }
    
    if packages is None:
        packages = lookup.keys()

    for package, apps in lookup.items():
        for app in apps:
            yield "'%s'" % app
        if package == 'blogs' and ('stories' in packages or 'blogs' in packages):
            yield "'positions'"

@format
def get_urls(apps):
    yield "(r'^cache/', include('django_memcached.urls'))"
    yield "(r'^admin/log/', include('logjam.urls'))"
    yield "(r'^admin/varnish/', include('varnishapp.urls'))"
    yield "(r'^admin_tools/', include('admin_tools.urls'))"
    yield "(r'^frontendadmin/', include('frontendadmin.urls'))"
    yield "(r'^registration/', include('registration.backends.default.urls'))"
    yield "(r'^accounts/', include('registration.urls'))"
    yield "(r'^profile/', include('profiles.urls'))"
    yield "url(r'^robots.txt', 'robots.views.rules_list', name='robots_rule_list')"
    
    if 'stories' in apps or 'blogs' in apps:
        yield "(r'^position_management/', include('positions.urls'))"
    if 'critic' in apps:
        yield "(r'^critic/', include('critic.urls'))"
    if 'api' in apps:
        yield "(r'^api/', include('api.urls'))"
    if 'synagg' in apps:
        yield "(r'^syn/', include('synagg.urls'))"
    if 'massmedia' in apps:
        yield "(r'^multimedia/', include('massmedia.urls'))"
    if 'news_sitemaps' in apps:
        yield "(r'^sitemaps/', include('news_sitemaps.urls'))"
    if 'stories' in apps:
        yield "(r'^news/', include('stories.urls'))"
    if 'mailfriend' in apps:
        yield "(r'^mail-a-friend/', include('mailfriend.urls'))"
    if 'categories' in apps:
        yield "(r'^categories/', include('categories.urls'))"
    if 'offensivecontent' in apps:
        yield "(r'^moderator/', include('offensivecontent.urls'))"
    if 'pollit' in apps:
        yield "(r'^polls/', include('pollit.urls'))"
    if 'staff' in apps:
        yield "(r'^staff/', include('staff.urls'))"
    if 'blogs' in apps:
        yield "(r'^blog/', include('viewpoint.urls'))"
    yield "(r'^$', 'django.views.generic.simple.direct_to_template', {'template':'homepage.html'})"

print get_apps()

def replace(repl, text):
    text = text.replace('/gitignore', '/.gitignore')
    for key, value in repl.iteritems():
        key,value = map(str,(key,value))
        text = text.replace('$$$$%s$$$$' % key, value)
    return text

def main(repl, dest, templ_dir):
    try:
        os.makedirs(dest)
    except OSError:
        pass
    
    for root, dirs, files in os.walk(templ_dir):
        for filename in files:
            source_fn = os.path.join(root, filename)
            dest_fn = replace(repl, os.path.join(dest, root.replace(templ_dir, ''), replace(repl, filename)))
            try:
                os.makedirs(os.path.dirname(dest_fn))
            except OSError:
                pass
            print 'Copying %s to %s' % (source_fn, dest_fn)
            should_replace = True
            for bl_item in BLACKLIST:
                if bl_item in dest_fn:
                    should_replace = False
            data = open(source_fn, 'r').read()
            if should_replace:
                data = replace(repl, data)
            open(dest_fn, 'w').write(data)
            os.chmod(dest_fn, os.stat(source_fn)[0])
    
    print "Making the virtual environment (%s)..." % repl['virtenv']
    create_env_cmds = [
        'source virtualenvwrapper_bashrc', 
        'cd %s' % dest,
        'mkvirtualenv --no-site-packages --distribute %s' % repl['virtenv'],
        'easy_install pip'
    ]
    create_pa_cmd = [
        'source virtualenvwrapper_bashrc',
        'cat > $WORKON_HOME/%s/bin/postactivate '\
        '<<END\n#!/bin/bash/\ncd %s\nEND\n'\
        'chmod +x $WORKON_HOME/%s/bin/postactivate' % (repl['virtenv'], dest,repl['virtenv'])
    ]
    call([';'.join(create_env_cmds)], env=os.environ, executable='/bin/bash', shell=True)
    call([';'.join(create_pa_cmd)], env=os.environ, executable='/bin/bash', shell=True)

    #print "Installing Calloway..."
    #calloway = os.path.join(os.path.dirname(__file__), '..')
    #call(['$WORKON_HOME/%s/bin/pip install -r %s' \
    #    % (repl['virtenv'], os.path.join(calloway, 'setup', 'requirements.txt'))],
    #    env=os.environ, executable='/bin/bash', shell=True, cwd=calloway)

    print "Installing requirements..."
    call(['$WORKON_HOME/%s/bin/pip install -r %s' \
        % (repl['virtenv'], os.path.join(dest, 'setup', 'requirements.txt'))],
        env=os.environ, executable='/bin/bash', shell=True, cwd=dest)

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    
    parser.add_option("-a", "--admin", dest="name", default=os.getlogin(), help="The name of the administrator.")
    parser.add_option("-e", "--email", dest="email_address", help="The email address of the administrator.")
    parser.add_option("-n", "--name", dest="project_name", help="The name of the project.")
    parser.add_option("-v", "--virtenv", dest="virtenv", help="The name of the virtualenv.")
    parser.add_option("-d", "--dest", dest="destination", help="Where to put the new project.")
    parser.add_option("-t", "--template", dest="template", help="The project template to use as a basis for the new project.")
    (options, args) = parser.parse_args()
    
    repl = {
        'EMAIL_ADDRESS':None, 
        'PROJECT_NAME':None,
        'NAME':None,}
    dest_dir = None
    templ_dir = None
    
    cur_user = os.getlogin()
    
    if options.project_name:
        repl['PROJECT_NAME'] = options.project_name
    elif len(args) > 0:
        repl['PROJECT_NAME'] = args[0]
    
    while not repl['PROJECT_NAME']:
        repl['PROJECT_NAME'] = raw_input('Project name: ')
    
    if options.name:
        repl['NAME'] = options.name
    
    while not repl['NAME']:
        repl['NAME'] = raw_input('Administrator name  [%s]: ' % cur_user) or cur_user
    
    if options.email_address:
        repl['EMAIL_ADDRESS'] = options.email_address
    
    while (not repl['EMAIL_ADDRESS'] or email_re.match(repl['EMAIL_ADDRESS']) is None):
        repl['EMAIL_ADDRESS'] = raw_input('Administrator e-mail address: ')
    
    repl['SECRET_KEY'] = ''.join([choice(CHARS) for i in xrange(50)])
    
    if options.destination:
        dest_dir = options.destination
    
    while not dest_dir:
        dest_dir = raw_input('Destination directory (currently at %s): ' % (os.getcwd(),)) or os.getcwd()
    dest_dir =  os.path.realpath(os.path.expanduser(dest_dir))
    dest = os.path.join(dest_dir, repl['PROJECT_NAME'])
    
    if options.template:
        templ_dir = options.template
    
    default = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'project_template'))
    while not templ_dir:
        templ_dir = raw_input('Project template directory [%s]: ' % default) or default
    templ_dir = os.path.realpath(os.path.expanduser(templ_dir))
    if templ_dir[-1] != '/':
        templ_dir = templ_dir + "/"
    if options.virtenv:
        repl['virtenv'] = options.virtenv
    
    repl['virtenv'] = None
    while not repl['virtenv']:
        repl['virtenv'] = raw_input('Virtual environment name [%s]: ' % repl['PROJECT_NAME']) or repl['PROJECT_NAME']
    
    packages = []
    for p in ['Media','Admin','Comments','Staff','Stories','Blogs','Categories',
                'Debug','Polls','Tagging','API','Utils','Registration','TinyMCE']:
        i = raw_input('Install %s Package [Y/n]? ' % p) or True
        if isinstance(i, basestring) and i.lower().startswith('n'):
            continue
        packages.append(p.lower())
        
    repl['INSTALLED_APPS'] = get_apps(packages)
    repl['MIDDLEWARE'] = get_middleware(repl['INSTALLED_APPS'])
    repl['URLS'] = get_urls(repl['INSTALLED_APPS'])
            
    main(repl, dest, templ_dir)