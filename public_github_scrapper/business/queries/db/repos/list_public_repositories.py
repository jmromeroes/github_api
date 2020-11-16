from typing import Dict, List

from public_github_scrapper.business.domain.repositories.repository_information import RepositoryInformation

from public_github_scrapper.business.persistence.db.repos_persistence import ReposPersistence

class ListPublicRepositories:
    def execute(self) -> List[RepositoryInformation]:
        return ReposPersistence.list_public_repositories()
