from typing import Dict, List

from public_github_scrapper.business.domain.users.user_information import UserInformation

from public_github_scrapper.business.persistence.db.users_persistence import GithubUserPersistence

import attr

@attr.s(auto_attribs=True)
class GetUserByUsername:
    username: str
    def execute(self) -> List[UserInformation]:
        return GithubUserPersistence.get_user_information(self.username)
