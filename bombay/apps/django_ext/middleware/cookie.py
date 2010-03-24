from django.contrib.auth.models import AnonymousUser
from django.conf import settings

COOKIE_USERNAME_KEY = getattr(settings, 'COOKIE_USERNAME_KEY', 'username')
DOMAIN = settings.SESSION_COOKIE_DOMAIN

class UsernameInCookieMiddleware(object):
    def process_response(self, request, response):
        if hasattr(request, 'user') and not isinstance(request.user, AnonymousUser):
            response.set_cookie(COOKIE_USERNAME_KEY, request.user.username, domain=DOMAIN)
        elif hasattr(request, 'user')  and isinstance(request.user, AnonymousUser) and COOKIE_USERNAME_KEY in request.COOKIES:
            response.delete_cookie(COOKIE_USERNAME_KEY, domain=DOMAIN)
        return response