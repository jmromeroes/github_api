import public_github_scrapper.business.user_information.UserInformation
import requests

class FetchUserPublicInfo:
    def execute(self, username: str) -> UserInformation:
        
        if not cohort:
            return None
        return self._build_cohort_dto(cohort)

    def _build_user_dto(self, user: Dict) -> UserInformation:
        return UserInformation(
            user["login"],
            user["url"]
        )
