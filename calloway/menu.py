from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from admin_tools.menu.models import *

# ADMIN_TOOLS_MENU = 'calloway.menu.DefaultMenuMenu'
class DefaultMenu(Menu):
    def __init__(self, **kwargs):
        super(DefaultMenu, self).__init__(**kwargs)
        self.children.append(
            MenuItem(title='Dashboard', url=reverse('admin:index'))
        )
        
        APPS = settings.INSTALLED_APPS
        content_children, organize_children = [], []
        settings_children, users_children = [], []
        comments_children = []
        
        # Content Menu
        if 'stories' in APPS:
            content_children.append(MenuItem(title='Stories', url=reverse('admin:stories_story_changelist')))
  
        if 'pollit' in APPS:
            content_children.append(MenuItem(title='Polls', url=reverse('admin:pollit_poll_changelist')))
            
        if 'viewpoint' in APS:
            content_children.append(MenuItem(title='Blog Entries', url=reverse('admin:viewpoint_entry_changelist')))
            organize_children.append(MenuItem(title='Blogs', url=reverse('admin:viewpoint_blog_changelist')))
        
        if 'massmedia' in APPS:
            content_children.append(MenuItem(title='Audio Clips', url=reverse('admin:massmedia_audio_changelist')))
            content_children.append(MenuItem(title='Collections', url=reverse('admin:massmedia_collection_changelist')))
            content_children.append(MenuItem(title='Documents', url=reverse('admin:massmedia_document_changelist')))
            content_children.append(MenuItem(title='Images', url=reverse('admin:massmedia_image_changelist')))
            content_children.append(MenuItem(title='Videos', url=reverse('admin:massmedia_video_changelist')))
            

        # Organize Menu
        if 'categories' in APPS:
            organize_children.append(MenuItem(title='Categories', url=reverse('admin:categories_category_changelist')))
            
        if 'hiermenu' in APPS:
            organize_children.append(MenuItem(title='Navigation Bar', url=reverse('admin:hiermenu_menu_changelist')))
            
        if 'positions' in APPS:
            organize_children.append(MenuItem(title='Postions', url=reverse('admin:positions_position_changelist')))
            
            
        # Settings Menu
        if 'google_analytics' in APPS:
            settings_children.append(MenuItem(title='Analytics', url=reverse('admin:google_analytics_analytics_changelist')))
            
        if 'django.contrib.redirects' in APPS:
            settings_children.append(MenuItem(title='Redirects', url=reverse('admin:redirects_redirect_changelist')))
            
        if 'robots' in APPS:
            settings_children.append(MenuItem(title='Robots', url=reverse('admin:app_list', args=('robots',))))
            
        if 'synagg' in APPS:
            settings_children.append(MenuItem(title='Syndication Feeds', url=reverse('admin:synagg_feed_changelist')))
            
            
        # Comments Menu
        if 'mptt_comments' in APPS:
            comments_children.append(MenuItem(title='Comments', url=reverse('admin:mptt_comments_mpttcomment_changelist')))
            
        if 'offensicecontent' in APPS:
            comments_children.append(MenuItem(title='Offensive Content', url=reverse('admin:offensivecontent_offensivecontent_changelist')))
            
            
        # Users Menu
        if 'django.contrib.auth' in APPS:
            users_children.append(MenuItem(title='Users', url=reverse('admin:auth_user_changelist')))
            
        if 'ban' in APPS:
            users_children.append(MenuItem(title='Banned IPs', url=reverse('admin:ban_deniedip_changelist')))
            
            
        # Set the Menu's
        self.children.append(
            MenuItem(title='Content', 
                children=content_children)
        )
        self.children.append(
            MenuItem(title='Organize', 
                children=organize_children)
        )
        self.children.append(
            MenuItem(title='Settings', 
                children=settings_children)
        )
        self.children.append(
            MenuItem(title='Comments', 
                children=comments_children)
        )
        self.children.append(
            MenuItem(title='Users', 
                children=users_children)
        )

