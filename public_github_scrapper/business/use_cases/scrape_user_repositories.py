from public_github_scrapper.business.queries.api.repos.fetch_repos_by_username import FetchRepositoriesByUsername
from public_github_scrapper.business.commands.base import CommandBase, CommandError, CommandResult

from public_github_scrapper.business.commands.db.save_user_repositories import SaveUserRepositories

import attr

import logging 
_logger = logging.getLogger(__name__)

@attr.s(auto_attribs=True)
class ScrapeRepositoriesByUsername(CommandBase):
    username: str
    def execute(self):
        try:
            repositories = FetchRepositoriesByUsername().execute(self.username)

            SaveUserRepositories(self.username, repositories).execute()

            _logger.info("Succesfully ran use case {}".format(type(self)))
            
            return CommandResult(is_success=True)
        except Exception as e:
            msg = "Error running use case {}".format(
                type(self)
            )
            _logger.error(msg)
            _logger.exception(e)
            
            raise CommandError(e).with_traceback(e.__traceback__)
