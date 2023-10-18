from rest_framework.response import Response
from rest_framework.views import APIView

from rest.service import Service

# Create your views here.
class CharacterAPIView(APIView):
    def get(self, request):
        service = Service()
        return Response(service.get_character(request=request.GET))
