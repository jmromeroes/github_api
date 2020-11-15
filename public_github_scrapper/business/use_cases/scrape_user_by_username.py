from public_github_scrapper.business.queries.api.users.fetch_user_public_info import FetchUserPublicInfo
from ..commands.base import CommandBase, CommandError, CommandResult

from ..commands.db.save_user import SaveUser

import attr

import logging

_logger = logging.getLogger(__name__)

@attr.s(auto_attribs=True)
class ScrapeUserByUsername(CommandBase):
    username: str
    
    def execute(self):
        try:
            user = FetchUserPublicInfo().execute(self.username)
            SaveUser(user).execute()

            _logger.info("Succesfully ran use case {}".format(type(self)))
        except Exception as e:
            msg = "Error running use case {}".format(
                type(self)
            )
            _logger.error(msg)
            _logger.exception(e)
            
            raise CommandError(e).with_traceback(e.__traceback__)
