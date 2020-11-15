from typing import Dict, List

from public_github_scrapper.business.domain.repositories.repository_information import RepositoryInformation
from ..github_query import GitHubQuery
from .builder import RepositoryBuilder

class FetchPublicRepositories(GitHubQuery):
    def execute(self) -> List[Dict]:
        return self.get("repositories")

    def _build_dto(self, repositories: List[Dict]) -> List[RepositoryInformation]:
        return RepositoryBuilder.build_dto(repositories)
