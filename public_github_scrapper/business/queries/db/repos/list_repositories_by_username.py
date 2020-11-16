from typing import Dict, List

from public_github_scrapper.business.domain.repositories.repository_information import RepositoryInformation
from public_github_scrapper.business.persistence.db.repos_persistence import ReposPersistence

import attr

@attr.s(auto_attribs=True)
class ListRepositoriesByUsername:
    username: str
    
    def execute(self) -> List[RepositoryInformation]:
        return ReposPersistence.list_user_repositories(self.username)
