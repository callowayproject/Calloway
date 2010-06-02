from django.core.management.base import NoArgsCommand
from django.db import transaction
from django.conf import settings
import os

class Command(NoArgsCommand):
    help = "Prints out a requirements file"

    def handle_noargs(self, **options):
        try:
            reqs = open(os.path.join(settings.CALLOWAY_ROOT, 'requirements.txt')).read()
        except IOError, e:
            print "Returned an error reading the requirements file: %s" % e
        
        print reqs
