import os
from django.core.management.base import BaseCommand, CommandError
from django.utils.simplejson import load
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.db.models import get_model
from categories.models import Category
from staff.models import StaffMember
import calloway

class Command(BaseCommand):
    
    def story(s):
        return s
    
    def entries(**kwargs):
        return 'viewpoint.entry', {
            'body': kwargs.pop('body'),
            'author': kwargs.pop('author'),
            'slug': kwargs.pop('slug'),
            'title': kwargs.pop('title'),
            'summary': kwargs.pop('tease'),
            'pub_date': kwargs.pop('pub_date'),
        }
    
    mapping = {
        'news.story': 'stories.story',
        'weblogs.entry': 'viewpoint.entry',
    }
    
    def handle(self, *args, **options):
        if not len(args):
            for arg in args:
                self.migrate(arg)
        else:
            for attr in dir(self):
                if attr.startswith('migrate_'):
                    self.migrate(attr[8:], *getattr(self, attr)())

    def get_fixture(self, name):
        adir = 'fixtures'
        for f in os.listdir(adir):
            if f.startswith(name):
                return load(open(os.path.join(adir, f)))
        raise IOError('Fixture %r not found' % name)
    
    def migrate(self, app):
        new_objs = []
        for obj in self.get_fixture(app):
            m = self.mapping[obj['model']].split('.')
            model = get_model(*m)
            
            kw,rel = getattr(self, m[-1])(**obj['fields'])
            if not 'pk' in kw:
                kw['pk'] = obj['pk']
            #for old,new in mapping.items():
            #    value = obj['fields'].get(old, None)
            #    if new in filters:
            #        value = filters[new](value)
            #    kw[new] = value
            #
            #rel = {}
            #for k in kw:
            #    if k in related:
            #        rel[k] = related[k](kw[k])
            #
            #for k in rel:
            #    kw.pop(k)
            #
            #if model == StaffMember:
            #    kw['user'] = User.objects.get_or_create(
            #            username = 'staff-%s' % kw['pk'],
            #            is_active=kw['is_active'],
            #            email=kw['email'],
            #            first_name=kw['first_name'],
            #            last_name=kw['last_name'])[0]

            o = model.objects.get_or_create(**kw)[0]
            for k,v in rel.items():
                for i in v:
                    getattr(o, k).add(i)
            new_objs.append(o)
        return new_objs
    
    def entries(self, **fields):
        return {
            'body': fields.pop('body'),
            'author': fields.pop('author'),
            'slug': fields.pop('slug'),
            'title': fields.pop('title'),
            'summary': fields.pop('tease'),
            'pub_date': fields.get('pub_date'),
            'pub_time': fields.get('pub_date'),
        }
    
    def migrate_staff(self):
        return 'staff.staffmember', {
                'bio': 'bio',
                'first_name': 'first_name',
                'last_name': 'last_name',
                'mugshot': 'photo',
                'is_active': 'is_active',
                'sites': 'sites',
                'email': 'email',
                'phone': 'phone',
                'slug': 'slug'
            }, {}, {}, {
                'sites': lambda l: map(lambda pk: Site.objects.get(pk=pk), l)
            }
    
    def migrate_stories(self):
        c = lambda v: Category.objects.get(pk=v)
        a = lambda v: StaffMember.objects.get(pk=v)
        return 'stories.story', {
                'headline': 'headline',
                'pub_date': 'publish_date',
                'story': 'body',
                'sites': 'site',
                'status': 'status',
                'print_headline': 'subhead',
                'status': 'status',
                'tease': 'teaser',
                'slug': 'slug',
                'primary_category': 'primary_category',
                'kicker':'kicker',
                'bylines':'authors',
                'categories': 'categories',
            },{
                'publish_date': lambda v: v.split()[0],
                'site': lambda v: Site.objects.get_current(),
                'primary_category': c,
                'categories': lambda v: None
            },{
            }, {
                'categories': lambda l: map(c, l or []),
                'authors': lambda l: map(a, l)
        }
        
    def migrate_images(self):
        return 'massmedia.image', {
                'creation_date': 'creation_date',
                'photographer': 'author',
                'one_off_photographer': 'one_off_author',
                'credit': 'credit',
                'caption': 'caption',
                'photo': 'file',
                'width': 'width',
                'height': 'height',
                'sites': 'sites',
                'categories':'categories',
            }
        
    def migrate_categories(self):
        return 'categories.category', {
                'slug':'slug',
                'parent':'parent',
                'name':'name',
            }, {
                'parent': lambda _: None
            }, {
            }
        
