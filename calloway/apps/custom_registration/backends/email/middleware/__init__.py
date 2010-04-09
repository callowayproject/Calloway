"""
Authenticate using a email address
"""
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

class EmailAuthenticationBackend(ModelBackend):
    """
    Authenticates a user against a email address.
    """
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(email=username.lower())
            return super(EmailAuthenticationBackend, self).authenticate(user.username, password)
        except User.DoesNotExist:
            return None
    
