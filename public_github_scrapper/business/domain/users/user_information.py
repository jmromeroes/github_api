import attr
from ..base import BaseValueObject

@attr.s(auto_attribs=True, frozen=True)
class UserInformation(BaseValueObject):
    login: str
    url: str
    id: str
    node_id: str
    avatar_url: str
    gravatar_id: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    site_admin: bool
    name: str
    blog: str
    public_repos: str
