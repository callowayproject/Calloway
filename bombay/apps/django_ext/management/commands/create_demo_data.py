import os, random
from django.core.management.base import BaseCommand, CommandError
from categories.management.commands.import_categories import Command as import_categories_cmd

fixtures_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)),'..','fixtures'))
random.seed()

class Command(BaseCommand):
    def handle(self, *args, **options):
        if len(args):
            for arg in args:
                attr = 'create_%s' % arg
                if not hasattr(self, attr):
                    raise CommandError('Demo data routine for %r not found' % arg)
                getattr(self, attr)()
        else:
            self.create_all_demo_data()
    
    def create_nav_bar(self):
        from navbar.models import NavBarEntry
        nav = [
            {"name": "News", "parent": None, "title": "News stories by topic", "url": "/news/", "user_type": "E", "path_type": "A", "order": 0}, 
            {"name": "Opinion", "parent": None, "title": "What we think about things", "url": "/opinion/", "user_type": "E", "path_type": "A", "order": 10},
            {"name": "Galleries", "parent": None, "title": "Photo essays on current events", "url": "/photos/galleries/", "user_type": "E", "path_type": "A", "order": 20},
            {"name": "Video", "parent": None, "title": "Video briefs", "url": "/video/", "user_type": "E", "path_type": "A", "order": 30},
            {"name": "Topics", "parent": None, "title": "Collections of stories on popular topics", "url": "/topics/", "user_type": "E", "path_type": "A", "order": 40}
        ]
        for item in nav:
            print "Creating Nav Bar Entry: %s" % (item['name'])
            nav_entry = NavBarEntry(**item)
            nav_entry.save()
    
    def create_categories(self):
        test_file = os.path.abspath(os.path.join(fixtures_path, 'demo_categories.txt'))
        print "Creating categories from %s" % test_file
        import_categories_cmd().execute(test_file)
    
    def create_staff(self):
        from django.contrib.auth.models import User
        from staff.models import update_staff_member
        
        first_names = ['Andrew','Beth','Claire','Darcy','Ethan','Isabella',
                        'Jacob','Kevin','Madison','Norman','Olivia','Patrick',]
        last_names = ['Smith','Johnson','Williams','Jones','Brown','Quick',
                        'Patterson','Soarez','Hensley',]
        
        for i in range(10):
            fname = random.choice(first_names)
            lname = random.choice(last_names)
            username = '%s%s' % (fname[0].lower(), lname.lower())
            email = '%s@example.com' % username
            print "Creating %s (%s %s)" % (username, fname, lname)
            try:
                user = User.objects.create_user(username, email, 'password')
                user.is_staff = True
                user.first_name = fname
                user.last_name = lname
                user.save()
                update_staff_member(user, user, True)
            except Exception, e:
                print 'Skipping due to conflict.'
    
    def create_stories(self):
        import datetime
        from django.template.defaultfilters import slugify
        from django.contrib.sites.models import Site
        from django_ext import markov
        from stories.models import Story
        from categories.models import Category
        from staff.models import StaffMember
        
        chain = markov.MarkovChain()
        staff = StaffMember.objects.all()[:]
        categories = Category.objects.all()[:]
        
        # Load the dictionary into the markov chain
        sentences = os.path.abspath(os.path.join(fixtures_path, 'demo_story_data.txt'))
        for line in open(sentences):
            words = line.strip().split()
            chain.add(words)

        # Let's generate 10 random stories
        for i in range(10):
            story_data = {'headline': " ".join(chain.random_output(15))}
            story_data['slug'] = slugify(story_data['headline'])[:30]
            
            # 25% chance of a subhead
            if random.randint(1,4) == 1:
                story_data['subhead'] = " ".join(chain.random_output(20))
            
            story_data['teaser'] = " ".join(chain.random_output())
            story_data['publish_date'] = datetime.datetime.now().date()
            story_data['publish_time'] = datetime.datetime.now().time()
            story_data['site'] = Site.objects.get_current()
            story_data['primary_category'] = random.choice(categories)
            
            # Create a story with 4-10 paragraphs with 1-4 sentences each
            body = []
            for j in range(0, random.randint(4,10)):
                p = []
                for i in range(0, random.randint(1,4)):
                    p.append(" ".join(chain.random_output()))
                body.append("<p>%s</p>" % " ".join(p))
            story_data['body'] = "\n".join(body)
            story = Story(**story_data)
            story.save()
            story.authors.add(random.choice(staff))
