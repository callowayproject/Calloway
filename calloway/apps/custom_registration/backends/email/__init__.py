import random

from django.db import models
from django.conf import settings
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from django.template.loader import render_to_string
from django.utils.hashcompat import sha_constructor
from django.core.mail import send_mail

from registration import signals
from registration.models import RegistrationProfile
from registration.backends.default import DefaultBackend
from forms import EmailRegistrationForm

class EmailOrUserNameAuthenticationBackend(ModelBackend):
    """
    Authenticates a user against a username or email address.
    """
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            try:
                user = User.objects.get(email__iexact=username)
            except User.DoesNotExist:
                return None
                
        if user and user.check_password(password):
            return user
        return None


class EmailBackend(DefaultBackend):
    def register(self, request, **kwargs):
        """
        Create and immediately log in a new user.
        
        Only require a  email to register, username is generated
        automatically and a password is random generated and emailed
        to the user.
        
        Activation is still required for account uses after specified number
        of days.
        """
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)
        
        email = kwargs['email']
        
        # Generate random password
        password = User.objects.make_random_password()
        
        # Generate username based off of the email supplied
        username = sha_constructor(str(email)).hexdigest()[:30]
        
        incr = 0
        # Ensure the generated username is in fact unqiue
        while User.objects.filter(username=username).count() > 0:
            incr += 1
            username = sha_constructor(str(email + str(incr))).hexdigest()[:30]
        # Create the active user
        new_user = User.objects.create_user(username, email, password)
        new_user.save()
        
        # Create the registration profile, this is still needed because
        # the user still needs to activate there account for further users
        # after 3 days
        registration_profile = RegistrationProfile.objects.create_profile(
            new_user)
        
        # Authenticate and login the new user automatically
        auth_user = authenticate(username=username, password=password)
        login(request, auth_user)
        
        # Set the expiration to when the users browser closes so user
        # is forced to log in upon next visit, this should force the user
        # to check there email for there generated password.
        request.session.set_expiry(0)
        
        # Create a profile instance for the new user if 
        # AUTH_PROFILE_MODULE is specified in settings
        if hasattr(settings, 'AUTH_PROFILE_MODULE') and getattr(settings, 'AUTH_PROFILE_MODULE'):
            app_label, model_name = settings.AUTH_PROFILE_MODULE.split('.')
            model = models.get_model(app_label, model_name)
            try:
                profile = new_user.get_profile()
            except model.DoesNotExist:
                profile = model(user=new_user)
                profile.save()   
                
        # Custom send activation email
        self.send_activation_email(
            new_user, registration_profile, password, site)  
        
        # Send user_registered signal
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        return new_user

    def send_activation_email(self, user, profile, password, site):
        """
        Custom send email method to supplied the activation link and 
        new generated password.
        """
        ctx_dict = { 'password': password, 
                     'site': site, 
                     'activation_key': profile.activation_key,
                     'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS}
                     
        subject = render_to_string(
            'registration/email/emails/password_subject.txt',
            ctx_dict)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        
        message = render_to_string('registration/email/emails/password.txt',
                                   ctx_dict)
                                   
        try:
            user.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)
        except:
            pass
            

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


def handle_expired_accounts():
    """
    Check of expired accounts.
    """        
    for profile in RegistrationProfile.objects.all():
        # if registration profile is expired, deactive user.
        if profile.activation_key_expired():
            user = profile.user
            user.is_active = False
            user.save()
            
            # Send an email notifing user of there account becoming inactive.
            try:
                site = Site.objects.get_current()
                ctx_dict = { 'site': site, 
                             'activation_key': profile.activation_key}
                     
                subject = render_to_string(
                    'registration/email/emails/account_expired_subject.txt',
                    ctx_dict)
                subject = ''.join(subject.splitlines())
        
                message = render_to_string(
                    'registration/email/emails/account_expired.txt',
                    ctx_dict)
                user.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)
            except:
                pass
