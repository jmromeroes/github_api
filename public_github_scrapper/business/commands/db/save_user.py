from typing import List

import attr, cattr

from ..base import CommandBase, CommandError, CommandResult
from public_github_scrapper.business.domain.users.user_information import UserInformation
from public_github_scrapper.models.user_models import GithubUser
from django.core import serializers


@attr.s(auto_attribs=True)
class SaveUser(CommandBase):
    user: UserInformation

    def execute(self) -> CommandResult:
        try:
            user_dict = self.user.to_dict()

            if not GithubUser.objects.filter(node_id=user_dict["node_id"]).exists():
                return GithubUser.objects.create(**user_dict)
                
        except Exception as e:
            raise CommandError(e)
