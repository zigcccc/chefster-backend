from django.core.management.base import BaseCommand, CommandError
from users.models import User


class Command(BaseCommand):
    help = "Creates Chefster Admin User"

    def add_arguments(self, parser):
        parser.add_argument("--username", type=str)
        parser.add_argument("--password", type=str)
        parser.add_argument("--email", type=str)

    def handle(self, *args, **options):
        username = options["username"]
        email = options["email"]
        password = options["password"]

        u, created = User.objects.get_or_create(username=username, email=email)
        if created:
            u.is_superuser = True
            u.is_staff = True
            u.is_staff = True
            u.set_password(password)
            u.save()
        else:
            raise CommandError(f"chefster admin {username} already exist")

        return f"Chefster admin {username} successfully created!"
