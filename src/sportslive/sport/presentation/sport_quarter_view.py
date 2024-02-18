from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from sport.containers import SportContainer
from drf_yasg.utils import swagger_auto_schema
from sport.serializers import SportsQuarterResponseSerializer

class SportQuarterView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._sport_serivce = SportContainer.sport_service()
    
    @swagger_auto_schema(responses={"200": SportsQuarterResponseSerializer(many=True)})
    def get(self, request, sport_id: int):
        response = self._sport_serivce.get_all_quarter_list(sport_id)
        return Response(response, status=status.HTTP_200_OK)