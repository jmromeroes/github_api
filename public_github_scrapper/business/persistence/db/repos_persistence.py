from public_github_scrapper.models.repos_models import Repository
from public_github_scrapper.business.domain.repositories.repository_information import RepositoryInformation

import cattr
from django.core import serializers

import json

class ReposPersistence:

    @staticmethod
    class list_public_repositories():
        repositories = json.loads(serializers.serialize("json", Repository.objects.all()))
        domain_repositories = cattr.structure(repositories, List[RepositoryInformation])

        return domain_repositories

    @staticmethod
    class list_public_repositories(username: str):
        repositories = json.loads(serializers.serialize("json", Repository.objects.filter()))
        domain_repositories = cattr.structure(repositories, List[RepositoryInformation])

        return domain_repositories
