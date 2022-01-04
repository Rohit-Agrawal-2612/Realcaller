from django.core.management.base import BaseCommand, CommandError
from caller.models import UnauthUsers

class Command(BaseCommand):
    help = 'Creating fake data for unauthorised users'

    def handle(self, *args, **options):
        number = 1234567
        name = 'manu'

        for i in range(100):
            user = UnauthUsers(name=name+str(i), phone_number=number )
            user.save()
            number+=1
        self.stdout.write(self.style.SUCCESS('Successfully created fake data of unauthorised users'))