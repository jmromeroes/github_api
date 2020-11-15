from typing import List, Dict

from public_github_scrapper.business.domain.repositories.repository_information import RepositoryInformation
import cattr

class RepositoryBuilder:
    @staticmethod
    def build_dto(repository: List[Dict]) -> List[RepositoryInformation]:
        return cattr.structure(repository, List[RepositoryInformation])
