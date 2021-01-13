from django.db import models

class ESPNLeagues(models.Model):
    league_id = models.CharField(max_length=10, primary_key=True)
    priv = models.BooleanField()
    espn_s2 = models.CharField(max_length=400)
    swid = models.CharField(max_length=40)

class ESPNTeams(models.Model):
    league = models.ForeignKey('ESPNLeagues', on_delete=models.CASCADE)
    team_id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=30)
    abrv = models.CharField(max_length=4)
    division_name = models.CharField(max_length=25)
    logo_url = models.CharField(max_length=100)

class ESPNPlayers(models.Model):
    team = models.ForeignKey('ESPNTeams', on_delete=models.CASCADE)
    player = models.ForeignKey('Players', on_delete=models.CASCADE)

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

    