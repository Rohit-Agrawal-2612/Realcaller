from django.core.management.base import BaseCommand, CommandError
from caller.models import MyUser
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Creating fake data with email'

    def handle(self, *args, **options):
        number = 123456
        password = make_password("realcaller")
        name = 'rohit'
        email = 'rohit@realcaller.com'

        for i in range(100):
            user = MyUser(name=name+str(i),email=str(i)+email, password=password, phone_number=number )
            user.save()
            number+=1
        self.stdout.write(self.style.SUCCESS('Successfully created fake data with email'))