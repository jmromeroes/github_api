from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class PublicRepositoriesAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        pass

class PublicRepositoriesByUserAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, username):
        pass

class PublicBranchesByRepositoryAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, username, repository):
        pass
