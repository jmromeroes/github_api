from public_github_scrapper.business.queries.api.repos.fetch_public_repos import FetchPublicRepositories
from public_github_scrapper.business.commands.base import CommandBase, CommandError, CommandResult

from public_github_scrapper.business.commands.db.save_repositories import SaveRepositories

import attr

import logging 
_logger = logging.getLogger(__name__)

@attr.s(auto_attribs=True)
class ScrapePublicRepositories(CommandBase):
    def execute(self):
        try:
            repositories = FetchPublicRepositories().execute()

            SaveRepositories(repositories).execute()

            _logger.info("Succesfully ran use case {}".format(type(self)))
            
            return CommandResult(is_success=True)
        except Exception as e:
            msg = "Error running use case {}".format(
                type(self)
            )
            _logger.error(msg)
            _logger.exception(e)
            
            raise CommandError(e).with_traceback(e.__traceback__)
