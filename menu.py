from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from admin_tools.menu.models import *

# to activate your custom menu add the following to your settings.py:
#
# ADMIN_TOOLS_MENU = 'bombay.menu.CustomMenu'
class CustomMenu(Menu):
    def __init__(self, **kwargs):
        super(CustomMenu, self).__init__(**kwargs)
        self.children.append(
            MenuItem(title='Dashboard', url=reverse('admin:index'))
        )
        # self.children.append(
        #     AppListMenuItem(title='Applications')
        # )
        self.children.append(
            MenuItem(title='Content', 
                children=[
                    MenuItem(title='Audio Clips', url=reverse('admin:massmedia_audio_changelist')),
                    MenuItem(title='Collections', url=reverse('admin:massmedia_collection_changelist')),
                    MenuItem(title='Documents', url=reverse('admin:massmedia_document_changelist')),
                    MenuItem(title='Images', url=reverse('admin:massmedia_image_changelist')),
                    MenuItem(title='Stories', url=reverse('admin:stories_story_changelist')),
                    MenuItem(title='Videos', url=reverse('admin:massmedia_video_changelist')),
                ])
        )
        self.children.append(
            MenuItem(title='Organize', 
                children=[
                    MenuItem(title='Categories', url=reverse('admin:categories_category_changelist')),
                    MenuItem(title='Navigation Bar', url=reverse('admin:navbar_navbarentry_changelist')),
                    MenuItem(title='Postions', url=reverse('admin:positions_position_changelist')),
                ])
        )
        self.children.append(
            MenuItem(title='Settings', 
                children=[
                    MenuItem(title='Admin Menu'),
                    MenuItem(title='Analytics', url=reverse('admin:google_analytics_analytics_changelist')),
                    MenuItem(title='Denied IPs', url=reverse('admin:ban_deniedip_changelist')),
                    MenuItem(title='Redirects', url=reverse('admin:redirects_redirect_changelist')),
                    MenuItem(title='Robots', url=reverse('admin:app_list', args=('robots',))),
                    MenuItem(title='Syndication Feeds', url=reverse('admin:synagg_feed_changelist')),
                ])
        )
        self.children.append(MenuItem(title='Comments'))
        
        self.children.append(
            MenuItem(title='Users', 
                children=[
                    MenuItem(title='Users', url=reverse('admin:auth_user_changelist')),
                    # MenuItem(title='Profiles', url=reverse('admin:app_model_changelist')),
                ])
        )

