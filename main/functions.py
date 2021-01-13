from espn_api.basketball import League
from .models import *

current_season = 2021

def create_league(user_league, espn_league):
            
    for team in espn_league.teams:
        appended_id = str(user_league.league_id)+str(team.team_id)
        ESPNTeams.objects.update_or_create(
            league=user_league,
            team_id=appended_id,
            defaults=
                {
                    'name':team.team_name,
                    'abrv':team.team_abbrev,
                    'division_name':team.division_name,
                    'logo_url':team.logo_url
                }
        )
        for player in team.roster:
            try:
                nba = Players.objects.get(full_name=player.name)
            except Players.DoesNotExist as e:
                continue
            
            ESPNPlayers.objects.get_or_create(
                team=ESPNTeams(team_id=appended_id),
                player=Players(player_id=nba.player_id)
            )

def get_espn_league(l_id, season, priv, user_espn_s2, user_swid):
    try:
        if(priv):
            league = League(league_id=l_id, year=season, espn_s2=user_espn_s2, swid=user_swid)
        else:
            league = League(league_id=l_id, year=season)
    except Exception as e:
        return e
    return league