from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPI(APIView):
    def get(self, request):
        return Response({"message": "Hewwoooo world!"}, status=status.HTTP_200_OK)

# Create your views here.
