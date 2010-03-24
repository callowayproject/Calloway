from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate

attrs_dict = {'class': 'required'}

class EmailRegistrationForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(
                attrs=dict(attrs_dict,
                maxlength=75)),
                label=_("Email address"))
    
    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.
        
        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_(
                "This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']
        
        
class EmailAuthenticationForm(forms.Form):
    """
    Authentication form for email/password login's
    """
    email = forms.CharField(label=_("Email"), max_length=255)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(EmailAuthenticationForm, self).__init__(*args, **kwargs)
    
    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email__iexact=email)
            except User.DoesNotExist:
                raise forms.ValidationError(_("Please enter a correct username and password. Note that both fields are case-sensitive."))
            
            self.user_cache = authenticate(username=user.username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(_("Please enter a correct username and password. Note that both fields are case-sensitive."))
            elif not self.user_cache.is_active:
                raise forms.ValidationError(_("This account is inactive."))

        # TODO: determine whether this should move to its own method.
        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError(_("Your Web browser doesn't appear to have cookies enabled. Cookies are required for logging in."))

        return self.cleaned_data
    
    def get_user(self):
        return self.user_cache

