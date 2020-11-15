from typing import Dict

from public_github_scrapper.business.domain.users.user_information import UserInformation
from ..github_query import GitHubQuery

import cattr

class FetchUserPublicInfo(GitHubQuery):
    def execute(self, username: str) -> UserInformation:
        return self.get("users/{}".format(username))

    def _build_dto(self, user: Dict) -> UserInformation:
        return cattr.structure(user, UserInformation)
