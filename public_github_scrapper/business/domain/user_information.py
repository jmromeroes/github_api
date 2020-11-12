import attr

@attr.s(auto_attribs=True, frozen=True)
class UserInformation:
    username: str
    url: str

    @staticmethod
    def create_new():
        return UserInformation(
            username,
            url
        )
