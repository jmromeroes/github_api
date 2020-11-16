from public_github_scrapper.models.user_models import GithubUser
from public_github_scrapper.models.repos_models import Repository

from public_github_scrapper.business.domain.users.user_information import UserInformation

from typing import List

import cattr
from django.core import serializers

import json

class GithubUserPersistence:
    
    @staticmethod
    def get_user_information(username: str) -> UserInformation:
        user = list(map(lambda u: u["fields"], json.loads(serializers.serialize("json", GithubUser.objects.filter(login=username)))))

        return cattr.structure(user, List[UserInformation])

        
    @staticmethod
    def save_user_information(user: UserInformation):
        user_dict = user.to_dict()

        if not GithubUser.objects.filter(login=user_dict["login"]).exists():
            return GithubUser.objects.create(**user_dict)
