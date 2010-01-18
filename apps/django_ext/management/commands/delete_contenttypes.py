from django.core.management.base import NoArgsCommand
from django.db import transaction

class Command(NoArgsCommand):
    help = "Delete contenttypes crapola"

    def handle_noargs(self, **options):
        from django.db import connection
        print "Deleting content types and permissions"
        transaction.commit_unless_managed()
        transaction.enter_transaction_management()
        transaction.managed(True)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM django_content_type", [])
        print cursor.fetchall()
        cursor.execute("DELETE FROM auth_permission", [])
        print cursor.fetchall()
        transaction.commit()
        transaction.leave_transaction_management()
        print "Contenttypes deleted"