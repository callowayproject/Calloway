from sys import stderr
from django.conf import settings
from django.core.urlresolvers import reverse, NoReverseMatch
from django.utils.translation import ugettext_lazy as _
from admin_tools.menu.models import *

# ADMIN_TOOLS_MENU = 'calloway.menu.DefaultMenuMenu'
MENU_DEBUG = getattr(settings, 'ADMIN_TOOLS_MENU_DEBUG', False)

MENU_ITEMS = getattr(settings, 'ADMIN_TOOLS_MENU_ITEMS', (
    ('Dashboard', 'admin:index'),
    ('Content', [
        ('Stories', 'admin:stories_story_changelist'),
        ('Polls', 'admin:pollit_poll_changelist'),
        ('Blog Entries', 'admin:viewpoint_entry_changelist'),
        ('Audio Clips', 'admin:massmedia_audio_changelist'),
        ('Collections', 'admin:massmedia_collection_changelist'),
        ('Documents', 'admin:massmedia_document_changelist'),
        ('Images', 'admin:massmedia_image_changelist'),
        ('Videos', 'admin:massmedia_video_changelist'),
    ]),
    ('Organize', [
        ('Blogs', 'admin:viewpoint_blog_changelist'),
        ('Categories', 'admin:categories_category_changelist'),
        ('Navigation Bar', 'admin:hiermenu_menu_changelist'),
        ('Postions', 'admin:positions_position_changelist'),
    ]),
    ('Settings', [
        ('Analytics', 'admin:google_analytics_analytics_changelist'),
        ('Redirects', 'admin:redirects_redirect_changelist'),
        ('Robots', {'viewname':'admin:app_list', 'args':('robots',)}),
        ('Syndication Feeds', 'admin:synagg_feed_changelist'),
    ]),
    ('Comments', [
        ('Comments', 'admin:mptt_comments_mpttcomment_changelist'),
        ('Offensive Content', 'admin:offensivecontent_offensivecontent_changelist'),
    ]),
    ('Users', [
        ('Users', 'admin:auth_user_changelist'),
        ('Banned IPs', 'admin:ban_deniedip_changelist'),
    ]),
))


class DefaultMenu(Menu):
    
    def get_url(self, url_or_dict):
        """
        Returns the reversed url given a string or dict and prints errors if MENU_DEBUG is enabled
        """
        if isinstance(url_or_dict, basestring):
            url_or_dict = {'viewname': url_or_dict}
        try:
            return reverse(**url_or_dict)
        except NoReverseMatch:
            if MENU_DEBUG:
                print >>stderr,'Unable to reverse URL with kwargs %s' % url_or_dict
                
    def __init__(self, **kwargs):
        super(DefaultMenu, self).__init__(**kwargs)
        
        for section,item in MENU_ITEMS:
            if isinstance(item, basestring):
                self.children.append(MenuItem(title=section, url=reverse(item)))
            else:
                children = []
                for title,url in item:
                    url = self.get_url(url)
                    if url is None:
                        continue
                    children.append(MenuItem(title=title, url=url))
                self.children.append(MenuItem(title=section, children=children))
