from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from game.containers import GameContainer
from drf_yasg.utils import swagger_auto_schema
from game.serializers import GameChangeSerializer

class GameChangeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._game_serivce = GameContainer.game_service()

    @swagger_auto_schema(request_body=GameChangeSerializer, responses={"200": ''})
    def put(self, request, game_id: int, *args, **kwargs):
        self._game_serivce.change_game(game_id, request.data, request.user)
        return Response(status=status.HTTP_200_OK)