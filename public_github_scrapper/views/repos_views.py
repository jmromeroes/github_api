from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from public_github_scrapper.business.use_cases.scrape_public_repositories import ScrapePublicRepositories
from public_github_scrapper.business.use_cases.scrape_user_repositories import ScrapeRepositoriesByUsername


from public_github_scrapper.business.queries.exceptions import NotFoundQueryException, BadRequestQueryException, InternalServerException

import json

class PublicRepositoriesByUserAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, username):
        try:
            query_result = ScrapeRepositoriesByUsername(username).execute()

            return Response({})
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
            query_result = ScrapePublicRepositories().execute()

            return Response({})
        except Exception as e:
            print(e)
            return Response(
                {"error": "Internal server error"},
                status.HTTP_500_INTERNAL_SERVER_ERROR
            )
