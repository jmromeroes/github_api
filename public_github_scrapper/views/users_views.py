from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ..business.use_cases.scrape_user_by_username import ScrapeUserByUsername

import json

from public_github_scrapper.business.queries.exceptions import NotFoundQueryException, BadRequestQueryException, InternalServerException

class UserAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, username):
        try:
            user_query_result =  ScrapeUserByUsername(username).execute()
            return Response({})
        except Exception as e:
            print(e)
            return Response(
                {"error": "Internal server error"},
                status.HTTP_500_INTERNAL_SERVER_ERROR
            )
