from django.urls import path
from .views.users import UserAPI
from .views.repos import PublicRepositoriesAPI, PublicRepositoriesByUserAPI, PublicBranchesByRepositoryAPI
from .views.sns_handlers import HandleSectionCompletedNotification, HandleLearningStartedNotification

urlpatterns = [
    # Users Views
    path(
        "users/<username>",
        UserAPI.as_view(),
        name="user_information"
    ),
    path(
        "users/<username>/followers",
        UserAPI.as_view(),
        name="user_followers_information"
    ),
    path(
        "users/<username>/following",
        UserAPI.as_view(),
        name="user_following_information"
    ),

    #Repositories Views
    path(
        "repos",
        PublicRepositoriesAPI,
        name="repositories"
    ),
    path(
        "repos/<username>",
        PublicRepositoriesByUserAPI.as_view(),
        name="repositories_by_username"
    ),
    path(
        "repos/<username>/<repository>/branches",
        PublicBranchesByRepositoryAPI.as_view(),
        name="repository_branch"
    ),
    path(
        "repos/<owner>/<repository>/contributors",
        PublicBranchesByRepositoryAPI.as_view(),
        name="repository_branch"
    )
]
