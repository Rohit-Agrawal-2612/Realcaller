from django.core.management.base import BaseCommand, CommandError
from caller.models import MyUser
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Creating fake data'

    def handle(self, *args, **options):
        number = 12345
        password = make_password("realcaller")
        name = 'rohit'

        for i in range(100):
            user = MyUser(name=name+str(i), password=password, phone_number=number )
            user.save()
            number+=1
        self.stdout.write(self.style.SUCCESS('Successfully created fake data'))