from public_github_scrapper.business.use_cases.scrape_user_by_username import ScrapeUserByUsername
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Indicates the email of the user to scrape information from')
        
    def handle(self, *args, **options):
        try:
            username = options['username']
            query_result = ScrapeRepositoriesByUsername(username).execute()

            self.stdout.write(self.style.SUCCESS('Successfully scrapped repositories'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR('Error scrapping repositories {}'.format(e)))
