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
            MenuItem(title='My Content', 
                children=[
                    MenuItem(title='Entries'),
                    MenuItem(title='Neighborhoods'),
                    MenuItem(title='Static Pages'),
                    MenuItem(title='Breaking News'),
                    MenuItem(title='Audio'),
                ])
        )
        self.children.append(
            MenuItem(title='Organize', 
                children=[
                    MenuItem(title='Communties'),
                    MenuItem(title='Slots'),
                ])
        )
        self.children.append(
            MenuItem(title='Settings', 
                children=[
                    MenuItem(title='Admin Menu'),
                    MenuItem(title='SEP'),
                    MenuItem(title='Sites'),
                    MenuItem(title='Redirects'),
                    MenuItem(title='Robots'),
                ])
        )
        self.children.append(MenuItem(title='Comments'))
        
        self.children.append(
            MenuItem(title='Users', 
                children=[
                    MenuItem(title='Users'),
                    MenuItem(title='Staff Members'),
                    MenuItem(title='Profiles'),
                ])
        )

