from django.urls import path
from .views.users_views import UserAPI
from .views.repos_views import PublicRepositoriesAPI, PublicRepositoriesByUserAPI

urlpatterns = [
    # Users Views
    path(
        "users/<username>",
        UserAPI.as_view(),
        name="user_information"
    ),
    
    #Repositories Views
    path(
        "repositories",
        PublicRepositoriesAPI.as_view(),
        name="repositories"
    ),
    path(
        "users/<username>/repositories",
        PublicRepositoriesByUserAPI.as_view(),
        name="repositories_by_username"
    )
]
