from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username='test').exists():
            User.objects.create_superuser('test', 'test@test.com', 'test')
            print('Superuser created')
        else:
            print('Superuser already exists')