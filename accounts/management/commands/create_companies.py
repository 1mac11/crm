from django.core.management.base import BaseCommand
from company.models import Company


class Command(BaseCommand):
    help = 'Creates test Companies'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='count of necessary employees')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(count):
            company = Company.objects.create(name=f'company{i + 1}',
                                             owner_id=1,
                                             phone='998999698757',
                                             email=f'company{i + 1}@gmail.com'
                                             )
            company.employee.add()

        print(f'Created {count} test Companies')
