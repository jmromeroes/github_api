from typing import Dict, List

from public_github_scrapper.business.domain.repositories.repository_information import RepositoryInformation
from ..github_query import GitHubQuery
from .builder import RepositoryBuilder

class FetchRepositoriesByUsername(GitHubQuery):
    def execute(self, username: str) -> List[RepositoryInformation]:
        return self.get("users/{}/repos".format(username))

    def _build_dto(self, repository: List[Dict]) -> List[RepositoryInformation]:
        return RepositoryBuilder.build_dto(repository)
