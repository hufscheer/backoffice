from game.domain import GameRepository, LineupPlayer, GameTeam
from game.serializers import LineupPlayerGetSerializer, GameTeamInfoSerializer

class GameTeamGetService:
    def __init__(self, game_repository: GameRepository, *args, **kwargs):
        self._game_repository = game_repository

    def get_all_lineup_players(self, game_team_id: int):
        lineup_players: list[LineupPlayer] = self._game_repository.find_lineup_players_by_game_team_id(game_team_id)
        lineup_player_get_serializer = LineupPlayerGetSerializer(lineup_players, many=True)
        return lineup_player_get_serializer.data
    
    def get_game_teams_info(self, game_id: int):
        game_teams: list[GameTeam] = self._game_repository.find_game_teams_with_team_by_game_id(game_id)
        game_team_info_serializer = GameTeamInfoSerializer(game_teams, many=True)
        return game_team_info_serializer.data