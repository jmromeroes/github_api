from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ..business.queries.fetch_user_public_info import FetchUserPublicInfo

import json

from public_github_scrapper.business.queries.exceptions import NotFoundQueryException, BadRequestQueryException, InternalServerException

class UserAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, username):
        try:
            user_query_result =  FetchUserPublicInfo().execute(username)
            return json.dumps(user_public_information.__dict__)
        except NotFoundQueryException:
            return Response(
                {"error": "Username was not found in Github API"},
                status.HTTP_404_NOT_FOUND
            )
        except Exception:
            return Response(
                {"error": "Internal server error"},
                status.HTTP_500_INTERNAL_SERVER_ERROR
            )
