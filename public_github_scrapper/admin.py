from django.contrib import admin

from .models.repos_models import Repository
from .models.user_models import GithubUser

@admin.register(Repository)
class RepositoryAdmin(admin.ModelAdmin):
    pass


@admin.register(GithubUser)
class GithubUserAdmin(admin.ModelAdmin):
    pass
