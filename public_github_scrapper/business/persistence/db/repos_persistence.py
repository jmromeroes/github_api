from public_github_scrapper.models.repos_models import Repository
from public_github_scrapper.models.user_models import GithubUser
from public_github_scrapper.business.domain.repositories.repository_information import RepositoryInformation

import cattr
from django.core import serializers

import json

from typing import List

class ReposPersistence:

    @staticmethod
    def list_public_repositories():
        repositories = list(map(lambda u: u["fields"], json.loads(serializers.serialize("json", Repository.objects.all()))))
        domain_repositories = cattr.structure(repositories, List[RepositoryInformation])

        return domain_repositories

    @staticmethod
    def list_user_repositories(username: str):
        owner = GithubUser.objects.get(login=username)
        repositories = list(map(lambda u: u["fields"], json.loads(serializers.serialize("json", Repository.objects.filter(owner=owner)))))
        domain_repositories = cattr.structure(repositories, List[RepositoryInformation])

        return domain_repositories

    @staticmethod
    def save_repositories(repositories: List[RepositoryInformation]):
         for repository in repositories:
            repository_dict = repository.to_dict()

            if not Repository.objects.filter(node_id=repository_dict["node_id"]).exists():
                Repository.objects.create(**repository_dict)

    @staticmethod
    def save_user_repositories(username: str, repositories: List[RepositoryInformation]):
        owner = GithubUser.objects.get(login=username)
            
        for repository in repositories:
            repository_dict = repository.to_dict()

            if not Repository.objects.filter(node_id=repository_dict["node_id"]).exists():
                Repository.objects.create(**repository_dict, owner=owner)
                
            
