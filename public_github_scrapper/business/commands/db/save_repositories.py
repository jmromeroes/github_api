from typing import List

import attr, cattr
import json

from ..base import CommandBase, CommandError, CommandResult
from public_github_scrapper.business.domain.repositories.repository_information import RepositoryInformation

from django.core import serializers

from public_github_scrapper.business.persistence.db.repos_persistence import ReposPersistence
from public_github_scrapper.models.repos_models import Repository

@attr.s(auto_attribs=True)
class SaveRepositories(CommandBase):
    repositories: List[RepositoryInformation]

    def execute(self) -> CommandResult:
        try:
            ReposPersistence.save_repositories(self.repositories)
            
            return CommandResult(is_success=True)
        except Exception as e:
            raise CommandError(e)
