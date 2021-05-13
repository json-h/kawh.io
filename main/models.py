from django.db import models

# Contains ESPN league details/credentials, can reuse to retrieve data again
class ESPNLeagues(models.Model):
    league_id = models.CharField(max_length=10, primary_key=True)
    # This field checks if the league is private or not
    priv = models.BooleanField()
    espn_s2 = models.CharField(max_length=400)
    swid = models.CharField(max_length=40)

# User ESPN team details - M-1 relationship w/ above
class ESPNTeams(models.Model):
    league = models.ForeignKey('ESPNLeagues', on_delete=models.CASCADE)
    team_id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=30)
    abrv = models.CharField(max_length=4)
    division_name = models.CharField(max_length=25)
    logo_url = models.CharField(max_length=100)

# User rosters - M-1 relationship with teams and nba players
class ESPNPlayers(models.Model):
    team = models.ForeignKey('ESPNTeams', on_delete=models.CASCADE)
    player = models.ForeignKey('Players', on_delete=models.CASCADE)

# ----- Starting from here, all tables are maintained and worked on outside of Django -----

# Game data - retrieved automatically from nba.net api - M-1 relationship w/ players
class Games(models.Model):
    season = models.CharField(max_length=5)
    week = models.IntegerField(default=0)
    player = models.ForeignKey('Players', on_delete=models.CASCADE)
    game_id = models.CharField(max_length=15)
    game_date = models.DateField(null=True)
    home_id = models.IntegerField(default=0)
    visitor_id = models.IntegerField(default=0)
    mins = models.IntegerField(default=0)
    fgm = models.IntegerField(default=0)
    fga = models.IntegerField(default=0)
    fgpct = models.DecimalField(max_digits=4, decimal_places=3)
    fg3m = models.IntegerField(default=0)
    fg3a = models.IntegerField(default=0)
    fg3pct = models.DecimalField(max_digits=4, decimal_places=3)
    ftm = models.IntegerField(default=0)
    fta = models.IntegerField(default=0)
    ftpct = models.DecimalField(max_digits=4, decimal_places=3)
    pts = models.IntegerField(default=0)
    off_reb = models.IntegerField(default=0)
    def_reb = models.IntegerField(default=0)
    tot_reb = models.IntegerField(default=0)
    ast = models.IntegerField(default=0)
    stl = models.IntegerField(default=0)
    blk = models.IntegerField(default=0)
    tov = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'games'

# Player details - M-1 with teams
class Players(models.Model):
    player_id = models.IntegerField(primary_key=True)
    team = models.ForeignKey('Teams', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    jersey = models.CharField(max_length=2)
    years_pro = models.IntegerField(null=True)
    position = models.CharField(max_length=10, null=True)

    class Meta:
        managed = False
        db_table = 'players'

    def __str__(self):
        return self.full_name

# NBA Team details    
class Teams(models.Model):
    team_id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=40, null=True)
    city = models.CharField(max_length=20, null=True)
    nickname = models.CharField(max_length=20, null=True)
    tricode = models.CharField(max_length=3, null=True)
    conference = models.CharField(max_length=4, null=True)
    division = models.CharField(max_length=15, null=True)

    class Meta:
        managed = False
        db_table = 'teams'

    def _str_(self):
        return self.full_name

# SQL View - average statistics of all games played
class LeagueAverage(models.Model):
    mins = models.DecimalField(max_digits=4, decimal_places=1)
    fgm = models.DecimalField(max_digits=4, decimal_places=1)
    fga = models.DecimalField(max_digits=4, decimal_places=1)
    ftm = models.DecimalField(max_digits=4, decimal_places=1)
    fta = models.DecimalField(max_digits=4, decimal_places=1)
    fg3m = models.DecimalField(max_digits=4, decimal_places=1)
    pts = models.DecimalField(max_digits=4, decimal_places=1)
    reb = models.DecimalField(max_digits=4, decimal_places=1)
    ast = models.DecimalField(max_digits=4, decimal_places=1)
    stl = models.DecimalField(max_digits=4, decimal_places=1)
    blk = models.DecimalField(max_digits=4, decimal_places=1)
    tov = models.DecimalField(max_digits=4, decimal_places=1)

    class Meta:
        managed = False
        db_table = 'league_averages'

# SQL View - individual player season averages, 1-1 to players
class SeasonAverages(models.Model):
    player = models.OneToOneField('Players', on_delete=models.CASCADE)
    gp = models.IntegerField()
    mins = models.DecimalField(max_digits=4, decimal_places=1)
    fgm = models.DecimalField(max_digits=4, decimal_places=1)
    fga = models.DecimalField(max_digits=4, decimal_places=1)
    fgpct = models.DecimalField(max_digits=4, decimal_places=3)
    ftm = models.DecimalField(max_digits=4, decimal_places=1)
    fta = models.DecimalField(max_digits=4, decimal_places=1)
    ftpct = models.DecimalField(max_digits=4, decimal_places=3)
    fg3m = models.DecimalField(max_digits=4, decimal_places=1)
    pts = models.DecimalField(max_digits=4, decimal_places=1)
    reb = models.DecimalField(max_digits=4, decimal_places=1)
    ast = models.DecimalField(max_digits=4, decimal_places=1)
    stl = models.DecimalField(max_digits=4, decimal_places=1)
    blk = models.DecimalField(max_digits=4, decimal_places=1)
    tov = models.DecimalField(max_digits=4, decimal_places=1)

    class Meta:
        managed = False
        db_table = 'season_averages_9cat'

# SQL View - individual std. deviations, 1-1 to players
class StandardDeviations(models.Model):
    player = models.OneToOneField('Players', on_delete=models.CASCADE)
    mins = models.DecimalField(max_digits=4, decimal_places=1)
    fgm = models.DecimalField(max_digits=4, decimal_places=1)
    fga = models.DecimalField(max_digits=4, decimal_places=1)
    fgpct = models.DecimalField(max_digits=4, decimal_places=3)
    ftm = models.DecimalField(max_digits=4, decimal_places=1)
    fta = models.DecimalField(max_digits=4, decimal_places=1)
    ftpct = models.DecimalField(max_digits=4, decimal_places=3)
    fg3m = models.DecimalField(max_digits=4, decimal_places=1)
    pts = models.DecimalField(max_digits=4, decimal_places=1)
    reb = models.DecimalField(max_digits=4, decimal_places=1)
    ast = models.DecimalField(max_digits=4, decimal_places=1)
    stl = models.DecimalField(max_digits=4, decimal_places=1)
    blk = models.DecimalField(max_digits=4, decimal_places=1)
    tov = models.DecimalField(max_digits=4, decimal_places=1)

    class Meta:
        managed = False
        db_table = 'standard_deviations'

# SQL View - league average std. deviation
class LeagueAverageStandardDeviation(models.Model):
    mins = models.DecimalField(max_digits=4, decimal_places=1)
    fgm = models.DecimalField(max_digits=4, decimal_places=1)
    fga = models.DecimalField(max_digits=4, decimal_places=1)
    fgpct = models.DecimalField(max_digits=4, decimal_places=3)
    ftm = models.DecimalField(max_digits=4, decimal_places=1)
    fta = models.DecimalField(max_digits=4, decimal_places=1)
    ftpct = models.DecimalField(max_digits=4, decimal_places=3)
    fg3m = models.DecimalField(max_digits=4, decimal_places=1)
    pts = models.DecimalField(max_digits=4, decimal_places=1)
    reb = models.DecimalField(max_digits=4, decimal_places=1)
    ast = models.DecimalField(max_digits=4, decimal_places=1)
    stl = models.DecimalField(max_digits=4, decimal_places=1)
    blk = models.DecimalField(max_digits=4, decimal_places=1)
    tov = models.DecimalField(max_digits=4, decimal_places=1)

    class Meta:
        managed = False
        db_table = 'league_average_stddev'

# SQL View - user teams averages
class ESPNTeamAverages(models.Model):
    team = models.OneToOneField('ESPNTeams', on_delete=models.CASCADE)
    mins = models.DecimalField(max_digits=4, decimal_places=1)
    fgm = models.DecimalField(max_digits=4, decimal_places=1)
    fga = models.DecimalField(max_digits=4, decimal_places=1)
    fgpct = models.DecimalField(max_digits=4, decimal_places=3)
    ftm = models.DecimalField(max_digits=4, decimal_places=1)
    fta = models.DecimalField(max_digits=4, decimal_places=1)
    ftpct = models.DecimalField(max_digits=4, decimal_places=3)
    fg3m = models.DecimalField(max_digits=4, decimal_places=1)
    pts = models.DecimalField(max_digits=4, decimal_places=1)
    reb = models.DecimalField(max_digits=4, decimal_places=1)
    ast = models.DecimalField(max_digits=4, decimal_places=1)
    stl = models.DecimalField(max_digits=4, decimal_places=1)
    blk = models.DecimalField(max_digits=4, decimal_places=1)
    tov = models.DecimalField(max_digits=4, decimal_places=1)

    class Meta:
        managed = False
        db_table = 'espn_team_averages'

# SQL View - user teams std. deviations
class ESPNTeamStandardDeviations(models.Model):
    team = models.OneToOneField('ESPNTeams', on_delete=models.CASCADE)
    mins = models.DecimalField(max_digits=4, decimal_places=1)
    fgm = models.DecimalField(max_digits=4, decimal_places=1)
    fga = models.DecimalField(max_digits=4, decimal_places=1)
    fgpct = models.DecimalField(max_digits=4, decimal_places=3)
    ftm = models.DecimalField(max_digits=4, decimal_places=1)
    fta = models.DecimalField(max_digits=4, decimal_places=1)
    ftpct = models.DecimalField(max_digits=4, decimal_places=3)
    fg3m = models.DecimalField(max_digits=4, decimal_places=1)
    pts = models.DecimalField(max_digits=4, decimal_places=1)
    reb = models.DecimalField(max_digits=4, decimal_places=1)
    ast = models.DecimalField(max_digits=4, decimal_places=1)
    stl = models.DecimalField(max_digits=4, decimal_places=1)
    blk = models.DecimalField(max_digits=4, decimal_places=1)
    tov = models.DecimalField(max_digits=4, decimal_places=1)

    class Meta:
        managed = False
        db_table = 'espn_team_stddev'

# SQL View - user teams week statistics
class ESPNWeekStatistics(models.Model):
    week = models.IntegerField()
    league = models.ForeignKey('ESPNLeagues', on_delete=models.CASCADE)
    team = models.ForeignKey('ESPNTeams', on_delete=models.CASCADE)
    fgpct = models.DecimalField(max_digits=4, decimal_places=3)
    ftpct = models.DecimalField(max_digits=4, decimal_places=3)
    fg3m = models.IntegerField()
    pts = models.IntegerField()
    reb = models.IntegerField()
    ast = models.IntegerField()
    stl = models.IntegerField()
    blk = models.IntegerField()
    tov = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'week_statistics'

    