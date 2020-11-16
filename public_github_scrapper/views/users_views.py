from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ..business.use_cases.scrape_user_by_username import ScrapeUserByUsername

import json

from public_github_scrapper.business.queries.exceptions import NotFoundQueryException, BadRequestQueryException, InternalServerException

from public_github_scrapper.business.queries.db.users.get_user_information import GetUserByUsername

class UserAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, username):
        try:
            user_query_result =  GetUserByUsername(username).execute()

            if len(user_query_result) == 0:
                return Response(
                    {"error": "User {} not found".format(username)},
                    status.HTTP_404_NOT_FOUND
                )
            return Response(user_query_result[0].to_json())
        except Exception as e:
            print(e)
            return Response(
                {"error": "Internal server error"},
                status.HTTP_500_INTERNAL_SERVER_ERROR
            )
