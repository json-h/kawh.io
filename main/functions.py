from espn_api.basketball import League

current_season = 2021

def get_espn_league(l_id, season, priv, user_espn_s2, user_swid):
    try:
        if(priv):
            league = League(league_id=l_id, year=season, espn_s2=user_espn_s2, swid=user_swid)
        else:
            league = League(league_id=l_id, year=season)
    except Exception as e:
        return e
    return league