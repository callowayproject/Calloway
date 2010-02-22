from django import http
from django.template import Context, loader
from django.contrib import admin
from django.views.decorators.cache import never_cache

def custom_server_error(request, template_name='500.html', admin_template_name='500A.html'):
    """
    500 error handler. Displays a full trackback for superusers and the first line of the
    traceback for staff members.

    Templates: `500.html` or `500A.html` (admin)
    Context: trace
        Holds the traceback information for debugging.
    """
    trace = None
    if request.user.is_authenticated() and (request.user.is_staff or request.user.is_superuser):
        try:
            import traceback, sys
            trace = traceback.format_exception(*(sys.exc_info()))
            if not request.user.is_superuser and trace:
                trace = trace[-1:]
            trace = '\n'.join(trace)
        except:
            pass
    
    # if url is part of the admin site, use the 500A.html template
    if request.path.startswith('/%s' % admin.site.name):
        template_name = admin_template_name
         
    t = loader.get_template(template_name) # You need to create a 500.html and 500A.html template.
    return http.HttpResponseServerError(t.render(Context({'trace': trace})))
custom_server_error = never_cache(custom_server_error)