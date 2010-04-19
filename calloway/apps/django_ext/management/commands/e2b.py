import os
from django.core.management.base import BaseCommand, CommandError
from django.utils.simplejson import load
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.db.models import get_model
from categories.models import Category
from staff.models import StaffMember
from stories.models import Story
import calloway

class Command(BaseCommand):
    def handle(self, *args, **options):
        if len(args):
            for arg in args:
                attr = 'migrate_%s' % arg
                if not hasattr(self, attr):
                    raise CommandError('Migration routine for %r not found' % arg)
                self.migrate(attr[8:], *getattr(self, attr)())
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
    
    def migrate(self, app, model, mapping, filters={}, attrs={}, related={}):
        new_objs = []
        model = get_model(*model.split('.'))
        for obj in self.get_fixture(app):
            kw = attrs.copy()
            kw['pk'] = obj['pk']
            for old,new in mapping.items():
                value = obj['fields'].get(old,None)
                if new in filters:
                    value = filters[new](value)
                kw[new] = value
            
            rel = {}
            for k in kw:
                if k in related:
                    rel[k] = related[k](kw[k])
            
            for k in rel:
                kw.pop(k)
                
            if model == StaffMember:
                kw['user'] = User.objects.get_or_create(
                        username = 'staff-%s' % kw['pk'],
                        is_active=kw['is_active'],
                        email=kw['email'],
                        first_name=kw['first_name'],
                        last_name=kw['last_name'])[0]
            elif model == Story:
                kw
            o = model.objects.get_or_create(**kw)[0]
            for k,v in rel.items():
                for i in v:
                    getattr(o, k).add(i)
            new_objs.append(o)
        return new_objs
    
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
        
