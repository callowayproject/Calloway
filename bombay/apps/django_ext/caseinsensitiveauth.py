from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import pre_save

from re import _alphanum

CHARS = getattr(settings, 'ALLOWED_USERNAME_CHARS', ''.join(_alphanum.keys()) + '-_')

class CaseInsensitiveModelBackend(object):
    def authenticate(self, username=None, password=None):
        if '@' in username: # I can has emailz addr
            try:
                user = User.objects.get(email=username)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                return 
        else: # I can haz uzerznamez
            username = filter(lambda c: c in CHARS, username).lower()
            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                return
            
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return

def username_formatter(sender, **kwargs):
    kwargs['instance'].username = kwargs['instance'].username.lower()

pre_save.connect(username_formatter, sender=User)
