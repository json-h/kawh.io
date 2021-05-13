from django.test import TestCase
from main.models import ESPNLeagues, ESPNTeams
from .functions import create_league, get_espn_league

class ImportTestCase(TestCase):
    
    def setUp(self):
        self.league = ESPNLeagues()
        self.league.league_id = "99158049"
        self.league.priv = '1'
        self.league.espn_s2 = "AECW3%2FuB3JBZq1gakFxDhzd7%2BdRtfTcMpJJFknlX2IDql%2BdgT12dF%2B8dQJcVr5XOoGJyc7KiREPF0vDIlt8O%2BttOr%2FoBzjMWqTQw5w1xuwwl7qdT6I7nCUCMuwiVS%2B%2B%2B5qKCbzcxoegcteRXbVtF08AT87jzOHy3%2F1y%2B7rmL3WKCPzFWfUvggpH%2FRyHcGRzxMpTBi3TvY3LEjotDBOVtoui96Kk0Jizmju%2B6hvghsinkyHitneJIsks5d4bFyN97Zz6xkiKlgWZD%2BHWUtLFfmv87dOng%2FzSwOaO0AcDsmIV1ZQ%3D%3D"
        self.league.swid = "{953A4BF0-A993-42C8-BA4B-F0A99332C8A5}"
        self.league.save()

        self.team = ESPNTeams()
        self.team.league = self.league
        self.team.team_id = "991580491"
        self.team.name = "Team 1"
        self.team.abrv = "T1"
        self.team.division_name = "East"
        self.team.logo_url = "www.google.com"
        self.team.save()

    def test_fields_team(self):
        query = ESPNTeams.objects.get(league=self.league)
        self.assertEqual(query, self.team)

    def test_retrieve(self):
        espn_league = get_espn_league(self.league.league_id, 2021, self.league.priv, self.league.espn_s2, self.league.swid)
        self.assertTrue(hasattr(espn_league, 'teams'))
