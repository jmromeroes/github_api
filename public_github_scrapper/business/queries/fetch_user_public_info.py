from typing import Dict

from public_github_scrapper.business.domain.user_information import UserInformation
from .github_query import GitHubQuery

class FetchUserPublicInfo(GitHubQuery):
    def execute(self, username: str) -> UserInformation:
        return self.get("users/{}".format(username))

    def _build_dto(self, user: Dict) -> UserInformation:
        return UserInformation(
            user["login"],
            user["url"]
        )
