from typing import List

import attr, cattr
import json

from ..base import CommandBase, CommandError, CommandResult
from public_github_scrapper.business.domain.repositories.repository_information import RepositoryInformation

from public_github_scrapper.business.persistence.db.repos_persistence import ReposPersistence

@attr.s(auto_attribs=True)
class SaveUserRepositories(CommandBase):
    username: str
    repositories: List[RepositoryInformation]

    def execute(self) -> CommandResult:
        try:
            ReposPersistence.save_user_repositories(self.username, self.repositories)
            
            return CommandResult(is_success=True)
        except Exception as e:
            raise CommandError(e)
