from public_github_scrapper.business.use_cases.scrape_public_repositories import ScrapePublicRepositories
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            query_result = ScrapePublicRepositories().execute()

            self.stdout.write(self.style.SUCCESS('Successfully scrapped repositories'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR('Error scrapping repositories {}'.format(e)))
