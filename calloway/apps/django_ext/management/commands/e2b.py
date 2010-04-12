import os
from django.core.management.base import BaseCommand, CommandError
from django.utils.simplejson import load
from django.contrib.sites.models import Site
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
        adir = os.path.join(os.path.dirname(calloway.__file__), 'fixtures')
        for f in os.listdir(adir):
            if f.startswith(name):
                return load(open(os.path.join(adir, f)))
        raise IOError('Fixture %r not found' % name)
    
    def migrate(self, app, model, mapping, filters={}, attrs={}):
        new_objs = []
        for obj in self.get_fixture(app):
            kw = attrs.copy()
            for old,new in mapping.items():
                value = obj['fields'][old]
                if new in filters:
                    value = filters[new](value)
                kw[new] = value
            new_objs.append(model.objects.get_or_create(**kw)[0])
        return new_objs
    
    def migrate_stories(self):
        from stories.models import Story
        from categories.models import Category
        
        return Story, {
                'headline': 'headline',
                'pub_date': 'publish_date',
                'story': 'body',
                'sites': 'site',
                'slug': 'slug'
            },{
                'publish_date': lambda v: v.split()[0],
                'site': lambda v: Site.objects.get_current(),
            },{
                'status':4,
                'primary_category': Category.objects.get_or_create(name='Uncategoriezed')[0]
            }
        
