from django.core.management.base import BaseCommand

from mes_aliments.data import Psql_data

class Command(BaseCommand):
    args = '<team_id>'
    help = 'Affiche la liste des backlogs'

    def handle(self, *args, **options):
    	self.psql_data = Psql_data()
