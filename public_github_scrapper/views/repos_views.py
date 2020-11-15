from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from public_github_scrapper.business.queries.api.repos.fetch_public_repos import FetchPublicRepositories
from public_github_scrapper.business.queries.api.repos.fetch_repos_by_username import FetchRepositoriesByUsername

from public_github_scrapper.business.queries.exceptions import NotFoundQueryException, BadRequestQueryException, InternalServerException

import json

class PublicRepositoriesByUserAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, username):
        try:
            query_result =  FetchRepositoriesByUsername().execute(username)

            return Response(json.dumps(list(map(lambda q: q.to_dict(), query_result))))
        except NotFoundQueryException:
            return Response(
                {"error": "Repositories for username were not found in Github API"},
                status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            print(e)
            return Response(
                {"error": "Internal server error"},
                status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class PublicRepositoriesAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        try:
            query_result = FetchPublicRepositories().execute()

            return Response(json.dumps(list(map(lambda q: q.to_dict(), query_result))))
        except Exception as e:
            print(e)
            return Response(
                {"error": "Internal server error"},
                status.HTTP_500_INTERNAL_SERVER_ERROR
            )
