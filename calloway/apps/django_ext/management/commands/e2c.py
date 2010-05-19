import os
from django.core.management.base import BaseCommand, CommandError
from django.utils.simplejson import load
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import get_model
from django.conf import settings

from categories.models import Category
from staff.models import StaffMember


def fix():
    if settings.DATABASE_ENGINE == 'postgresql_psycopg2':
        from django.db import connection, transaction
        cursor = connection.cursor()
    
        # Data modifying operation - commit required
        cursor.execute("""
        SELECT setval('"staff_staffmember_id_seq"', coalesce(max("id"), 1), max("id") IS NOT null) FROM "staff_staffmember";
        SELECT setval('"staff_staffmember_sites_id_seq"', coalesce(max("id"), 1), max("id") IS NOT null) FROM "staff_staffmember_sites";
        """)
        transaction.commit_unless_managed()
    
def getr(model):
    if isinstance(model, basestring):
        model = get_model(*model.split('.'))
    def inner(pk):
        try:
            return model.objects.get(pk=pk)
        except model.DoesNotExist:
            return
    return inner

class Command(BaseCommand):
    mapping = {
        'news.story': 'stories.story',
        'weblogs.entry': 'viewpoint.entry',
        'weblogs.blog': 'viewpoint.blog',
        'news.storyinlinemapping': 'stories.storyrelation',
    }
    order = ('staff','blogs','entries','stories','images','inlines')
    #order = ('inlines',)
    
    def handle(self, *apps, **options):
        if len(apps):
            for app in apps:
                self.migrate(app)
        for app in self.order:
            if app == 'staff':
                fix()
            print 'Migrating %s...' % app.title()
            self.migrate(app)
            if app == 'staff':
                fix()

    def get_fixtures(self, name):
        adir = 'fixtures'
        for f in os.listdir(adir):
            if f.startswith(name):
                f = os.path.join(adir, f)
                if os.path.isfile(f):
                    return [open(f)]
                elif os.path.isdir(f):
                    l = [os.path.join(f,x) for x in os.listdir(f) if x.endswith('.json')]
                    return sorted(map(open, l))
        raise IOError('Fixture %r not found' % name)
    
    def migrate(self, app):
        new_objs = []
        for fixture in self.get_fixtures(app):
            print 'Loading %s...' % fixture
            for obj in load(fixture):
                if obj['model'] in self.mapping:
                    m = self.mapping[obj['model']].split('.')
                else:
                    m = obj['model'].split('.')
                model = get_model(*m)
                if not model:
                    continue
                obj['fields'].update(pk=obj['pk'])
                try:
                    kw,rel = getattr(self, m[-1])(**obj['fields'])
                except AttributeError:
                    kw,rel = self.default(**obj['fields'])
                except TypeError:
                    continue
                if kw == rel == None:
                    continue
                if not 'pk' in kw:
                    kw['pk'] = obj['pk']
                if str(kw['pk']) in E:
                    continue
                from massmedia.models import Image
                try:
                    Image.objects.get(pk=kw['pk'])
                    continue
                except Image.DoesNotExist:
                    pass
                o = model(**kw)
                try:
                    Image.objects.get(slug=o.slug)
                    continue
                except Image.DoesNotExist:
                    o.slug = '_%s' % o.slug
                o.save()
                for k,v in rel.items():
                    for i in v:
                        getattr(o, k).add(i)
                new_objs.append(o)
        return new_objs
    
    def default(self, **fields):
        return fields, {}
        
    def storyrelation(self, **fields):
        from massmedia.models import Image
        from django.contrib.contenttypes.models import ContentType
        from stories.models import StoryRelation
        ctype = ContentType.objects.get_for_model(Image)
        if fields['inline_type'] == 'photo':
            story = getr('stories.story')(fields['story'])
            if story is None:
                return
            try:
                StoryRelation.objects.get(pk=fields['pk'])
                return
            except StoryRelation.DoesNotExist:
                return {
                    'story': story,
                    'content_type': ctype,
                    'object_id': fields['object_id'],
                    'relation_type': 'image'
                }, {}
            
        
    def staffmember(self, **fields):
        try:
            assert fields['email']
            user = User.objects.get(
                email=fields['email'],
                first_name = fields['first_name'],
                last_name = fields['last_name'],
            )
        except (User.DoesNotExist, AssertionError):
            user = User.objects.get_or_create(
                username = 'staffmember%d' % fields['pk'],
                email = fields['email'],
                first_name = fields['first_name'],
                last_name = fields['last_name'],
                is_active = False, is_staff = True
            )[0]

        return {
            'bio': fields['bio'],
            'first_name': fields['first_name'],
            'last_name': fields['last_name'],
            'photo': fields['mugshot'],
            'is_active': fields['is_active'],
            'email': fields['email'],
            'phone': fields['phone'],
            'slug': fields['slug'],
            'user': user
        }, {
            'sites': [Site.objects.get_current()],
        }
    
    def category(self, **fields):
        return {
            'rght': fields['rght'],
            'lft': fields['lft'],
            'level': fields['level'],
            'tree_id': fields['tree_id'],
            'slug': fields['slug'],
            'parent': fields['parent'] and getr(Category)(fields['parent']) or None,
            'name': fields['name'],
        }, {}
    
    def blog(self, **fields):
        owners = []
        for o in fields['authors']:
            user = getr('auth.user')(o)
            if user:
                try:
                    owners.append(StaffMember.objects.get(user=user))
                except:
                    break 
        return {
            'slug': fields['slug'],
            'title': fields['title'],
            'description': fields['description'] or '',
            'tease': fields.get('tagline', 'none') or 'none',
            'photo': fields['header_image'],
            'creation_date': fields['created_date'],
            'public': fields['display'],
        }, {
            'owners': owners,
        }
    
    def entry(self, **fields):
        user = getr(User)(fields.pop('author'))
        try:
            author = StaffMember.objects.get(user=user)
        except StaffMember.DoesNotExist:
            author = StaffMember.objects.create(user=user)
        cat = filter(None, map(getr(Category), fields['categories']))
        if len(cat):
            cat = cat[0]
        else:
            cat = None
        return {
            'blog': getr('viewpoint.blog')(fields['blog']),
            'body': fields['body'],
            'author': author,
            'slug': fields['slug'],
            'title': fields['title'],
            'tease': fields['summary'] or 'None',
            'pub_date': fields['pub_date'].split()[0],
            'pub_time': fields['pub_date'].split()[1],
            'category': cat
        }, {}
    
    def story(self, **fields):
        return {
            'headline': fields['headline'][:100],
            'publish_date': fields['pub_date'].split()[0],
            'publish_time': fields['pub_date'].split()[1],
            'body': fields['story'],
            'site': Site.objects.get_current(),
            'status': fields['status'],
            'subhead': fields['print_headline'],
            'teaser': fields['tease'],
            'slug': fields['slug'][:50],
            'primary_category': getr(Category)(fields['primary_category'] or 37) or getr(Category)(37),
            'kicker': fields['kicker'],
        }, {
            'authors': map(getr(StaffMember), fields['bylines']),
            'categories': filter(None, [getr(Category)(x or 37) for x in fields['categories']]),
        }
        
    def image(self, **fields):
        print fields
        return {
            'creation_date': fields['creation_date'],
            'author': getr(User)(fields['photographer']),
            'one_off_author': fields['one_off_photographer'],
            #'credit': fields['credit'],
            'caption': fields['caption'],
            'file': fields['photo'],
            'width': fields['width'],
            'height': fields['height'],
        }, {
            'sites': [Site.objects.get_current()],
            'categories': map(getr(Category), fields['categories']),
        }
