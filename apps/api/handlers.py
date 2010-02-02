from piston.handler import BaseHandler
from tagging.models import Tag, TaggedItem
from django.db.models import get_model
from django.core.urlresolvers import reverse
from pprint import pprint

class TagHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Tag
    
    def read(self, request):
        if 'referer' in request.GET:
            bits = filter(None, request.GET['referer'].replace('/admin/','').split('/'))
            model = get_model(*bits[:2])

            if len(bits) == 2:
                r = []
                for x in Tag.objects.cloud_for_model(model):
                    r.append({'size':x.font_size,'name':x.name})
                return r                  
            elif len(bits) == 3:
                if bits[2] == 'add':
                    return []
                obj = model.objects.get(pk=bits[2])
                tags = Tag.objects.get_for_object(obj)
                if 'tags' in request.GET:
                    obj.tags = request.GET['tags']
                else:
                    return tags
                
              
