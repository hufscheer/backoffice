from league.domain import LeagueRepository
from league.serializers import LeagueListGetSerializer
from league.domain import League, LeagueSport
from datetime import datetime
import pytz

class LeagueGetService:
    def __init__(self, league_repository: LeagueRepository):
        self._league_repository = league_repository

    def get_leagues(self, user_data):
        organization_id: int = user_data.organization_id
        leagues: list[League] = self._league_repository.find_all_leagues_with_sport_by_organization_id(organization_id)
        result_dict = self._classify_league_and_add_sport_data(leagues)
        league_get_serializer = LeagueListGetSerializer(self._ListWrapping(result_dict))
        return league_get_serializer.data
    
    def _classify_league_and_add_sport_data(self, leagues: list[League]):
        result_dict = {
            "playing": [],
            "scheduled": [],
            "finished": []
        }
        for league in leagues:
            league.sport_datas = [
                self._SportWrapping(league_sport)
                for league_sport in league.league_sports.all()
            ]
            result = self._classify_league(league)
            result_dict.get(result).append(league)
        return result_dict

    def _classify_league(self, league: League):
        timezone = pytz.timezone("Asia/Seoul")
        now = datetime.now(timezone)
        if league.start_at > now:
            return 'scheduled'
        elif league.start_at <= now < league.end_at:
            return 'playing'
        else:
            return 'finished'

    class _ListWrapping:
        def __init__(self, classified_leagues):
            self.playing = classified_leagues.get('playing')
            self.scheduled = classified_leagues.get('scheduled')
            self.finished = classified_leagues.get('finished')

    class _SportWrapping:
        def __init__(self, league_sport: LeagueSport):
            self.id = league_sport.sport.id
            self.name = league_sport.sport.name