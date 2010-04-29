from django.core.management.base import NoArgsCommand
from custom_registration.backends.email import handle_expired_accounts

class Command(NoArgsCommand):
    help = "Deactivate expired user from the database. This should be used when using the custom email registration backend."

    def handle_noargs(self, **options):
        handle_expired_accounts()
