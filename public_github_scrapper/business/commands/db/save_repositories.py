from typing import List

import attr, cattr
import json

from ..base import CommandBase, CommandError, CommandResult
from public_github_scrapper.business.domain.repositories.repository_information import RepositoryInformation

from django.core import serializers

from public_github_scrapper.models.repos_models import Repository

@attr.s(auto_attribs=True)
class SaveRepositories(CommandBase):
    repositories: List[RepositoryInformation]

    def execute(self) -> CommandResult:
        try:
            for repository in self.repositories:
                repository_dict = repository.to_dict()

                if not Repository.objects.filter(node_id=repository_dict["node_id"]).exists():
                    return Repository.objects.create(**repository_dict)
                    
        except Exception as e:
            raise CommandError(e)
