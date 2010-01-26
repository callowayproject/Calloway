import os
from django.core.management.base import BaseCommand, CommandError
from django.utils.simplejson import load
from django.contrib.sites.models import Site
import bombay

class Command(BaseCommand):
    def handle(self, *args, **options):
        if len(args):
            for arg in args:
                attr = 'migrate_%s' % arg
                if not hasattr(self, attr):
                    raise CommandError
                getattr(self, attr)()
        else:
            for attr in dir(self):
                if attr.startswith('migrate_'):
                    getattr(self, attr)()

    def get_fixture(self, name):
        adir = os.path.join(os.path.dirname(bombay.__file__), 'fixtures')
        for f in os.listdir(adir):
            if f.startswith(name):
                return load(open(os.path.join(adir, f)))
    
    def migrate(self, model, mapping, objs, overrides={}):
        new_objs = []
        for obj in objs:
            kw = {}
            for old,new in mapping.items():
                v = obj['fields'][old]
                if old in overrides:
                    v = overrides[old](v)
                kw[new] = v
            new_objs.append(model.objects.create(**kw))
        return new_objs
    
    def migrate_stories(self):
        from stories.models import Story
        
        print self.migrate(Story, {
            'headline': 'headline',
            'pub_date': 'publish_date',
            'story': 'body',
            'sites': 'site',
            'slug': 'slug'
        }, self.get_fixture('stories'), {
            'pub_date': lambda v: v.split()[0],
            'sites': lambda v: Site.objects.get_current(),
        })
        
