from django.core.management.base import BaseCommand, CommandError
from users.models import User

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--username")
        parser.add_argument("--password")
        parser.add_argument("--email")

    def handle(self, *args, **kwargs):
        user_admin = {
            "username": "admin",
            "password": "admin1234",
            "email": "admin@example.com"
        }

        username = kwargs["username"]
        password = kwargs["password"]
        email = kwargs["email"]

        if(username):
            user_admin["username"] = username
        
        if(password):
            user_admin["password"] = password

        if(email):
            user_admin["email"] = email
        
        test_username_exists = User.objects.filter(username=user_admin["username"])

        if(test_username_exists):
            raise CommandError('Username `%s` already taken.' % user_admin["username"])
        
        test_email_exists = User.objects.filter(email=user_admin["email"])

        if(test_email_exists):
            raise CommandError('Email `%s` already taken.' % user_admin["email"])

        User.objects.create_superuser(
            username=user_admin["username"],
            password=user_admin["password"],
            email=user_admin["email"]
        )

        self.stdout.write(self.style.SUCCESS('Admin `%s` successfully created!' % user_admin["username"]))
