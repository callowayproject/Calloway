from django.conf.urls.defaults import *
from piston.resource import Resource
from handlers import TagHandler

tag_handler = Resource(TagHandler)

urlpatterns = patterns('',
   url(r'^tags/?$', tag_handler),
)