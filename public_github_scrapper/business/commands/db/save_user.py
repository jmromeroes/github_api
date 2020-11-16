from typing import List

import attr, cattr

from ..base import CommandBase, CommandError, CommandResult
from public_github_scrapper.business.domain.users.user_information import UserInformation
from public_github_scrapper.business.persistence.db.users_persistence import GithubUserPersistence

@attr.s(auto_attribs=True)
class SaveUser(CommandBase):
    user: UserInformation

    def execute(self) -> CommandResult:
        try:
            GithubUserPersistence.save_user_information(self.user)

            return CommandResult(is_success=True)
        except Exception as e:
            raise CommandError(e)
