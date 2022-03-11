from django.core.management.base import BaseCommand
from users.models import User
from django.utils.crypto import get_random_string
import string
import random



USERS_QUANTITY = 2
class Command(BaseCommand):
    help = 'Create superuser, test_user'
    def random_email(self):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(5))+'@gmail.com'

    def handle(self, *args, **options):
        User.objects.create_superuser(username='superuser: '+get_random_string(length=3),
                                     email=self.random_email(),
                                     first_name='',
                                     last_name='',
                                     password='1')

        for i in range(USERS_QUANTITY):
            User.objects.create_user(username=get_random_string(length=3),
                                     email=self.random_email(),
                                     first_name='',
                                     last_name='', )
