from django.db import models

from .repos_models import Repository

class GithubUser(models.Model):
    login = models.CharField(max_length=150)
    url = models.CharField(max_length=150)
    id = models.CharField(max_length=150)
    node_id = models.CharField(max_length=150)
    avatar_url = models.CharField(max_length=150)
    gravatar_id = models.CharField(max_length=150)
    html_url = models.CharField(max_length=150)
    followers_url = models.CharField(max_length=150)
    following_url = models.CharField(max_length=150)
    gists_url = models.CharField(max_length=150)
    starred_url = models.CharField(max_length=150)
    subscriptions_url = models.CharField(max_length=150)
    organizations_url = models.CharField(max_length=150)
    repos_url = models.CharField(max_length=150)
    events_url = models.CharField(max_length=150)
    received_events_url = models.CharField(max_length=150)
    site_admin = models.BooleanField(default=True)
    name = models.CharField(max_length=150)
    blog = models.CharField(max_length=150)
    public_repos = models.CharField(max_length=150)
    repositories = models.ManyToManyField(Repository, verbose_name="list of repositories")
