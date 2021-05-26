import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from slugify import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        from django.conf import settings
        with open(settings.CSV_PATH, 'r') as csvfile:

            phone_reader = csv.DictReader(csvfile, delimiter=';')

            def into_model(line: dict):
                try:
                    entry = Phone(
                        name=line.get('name'),
                        image=line.get('image'),
                        price=int(line.get('price')),
                        release_date=line.get('release_date'),
                        lte_exists=line.get('lte_exists'),
                        slug=slugify(line.get('name')),
                    )

                    entry.save()
                    return entry

                except Exception as err:
                    print(err)

            [into_model(some_line) for some_line in phone_reader]
