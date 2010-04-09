import random

from django.db import models
from django.conf import settings
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.hashcompat import sha_constructor

from registration import signals
from forms import EmailRegistrationForm

class EmailBackend(object):
    def register(self, request, **kwargs):
        """
        Create and immediately log in a new user.
        
        Only require a  email to register, username is generated
        automatically and a password is random generated and emailed
        to the user.
        """
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)
        
        email = kwargs['email']
        # Generate a random password
        password = User.objects.make_random_password()
        
        # Generate a hash based off of the email supplied
        salt = sha_constructor(str(random.random())).hexdigest()[:5]
        # Only take 30 characters in order to fit in the username field
        username = sha_constructor(salt+email).hexdigest()[:29]
        
        test_username = username
        var = 1
        # Make sure the username is unique
        while len(User.objects.filter(username__iexact=test_username)):
            test_username = "%s%s" % (username, var)
            if not len(User.objects.filter(username__iexact=test_username)):
                username = test_username
                break
            var += 1
        
        # Create the new user
        user = User.objects.create_user(username, email, password)
        
        # Authenticate  and login the new user automatically
        new_user = authenticate(username=username, password=password)
        login(request, new_user)
        
        # Email the new password to the user
        self.send_password(new_user, password, site)
        
        # Create a profile instance for the new user if 
        # AUTH_PROFILE_MODULE is specified in settings
        if hasattr(settings, 'AUTH_PROFILE_MODULE'):
            app_label, model_name = settings.AUTH_PROFILE_MODULE.split('.')
            model = models.get_model(app_label, model_name)
            try:
                profile = new_user.get_profile()
            except model.DoesNotExist:
                profile = model(user=new_user)
                profile.save()        
        
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        return new_user

    def send_password(self, user, password, site):
        ctx_dict = { 'password': password, 'site': site }
        
        subject = render_to_string('registration/email/emails/password_subject.txt',
                                   ctx_dict)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        
        message = render_to_string('registration/email/emails/password.txt',
                                   ctx_dict)
        user.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)

    def activate(self, **kwargs):
        raise NotImplementedError

    def registration_allowed(self, request):
        """
        Indicate whether account registration is currently permitted,
        based on the value of the setting ``REGISTRATION_OPEN``. This
        is determined as follows:

        * If ``REGISTRATION_OPEN`` is not specified in settings, or is
          set to ``True``, registration is permitted.

        * If ``REGISTRATION_OPEN`` is both specified and set to
          ``False``, registration is not permitted.
        
        """
        return getattr(settings, 'REGISTRATION_OPEN', True)

    def get_form_class(self, request):
        return EmailRegistrationForm

    def post_registration_redirect(self, request, user):
        """
        After registration, redirect to the user's account page.
        
        """
        return ("/", (), {})
        #return (user.get_absolute_url(), (), {})

    def post_activation_redirect(self, request, user):
        raise NotImplementedError
