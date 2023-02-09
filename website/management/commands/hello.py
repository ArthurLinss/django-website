from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'hello world own command'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("hello world"))
