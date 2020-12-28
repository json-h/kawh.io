from django.db import models

class Games(models.Model):
    player = models.ForeignKey('Players', on_delete=models.CASCADE, null=True)
    game_id = models.CharField(max_length=15)
    game_date = models.DateField(null=True)
    fgm = models.IntegerField(default=0)
    fga = models.IntegerField(default=0)
    fg3m = models.IntegerField(default=0)
    fg3a = models.IntegerField(default=0)
    ftm = models.IntegerField(default=0)
    fta = models.IntegerField(default=0)
    pts = models.IntegerField(default=0)
    reb = models.IntegerField(default=0)
    ast = models.IntegerField(default=0)
    stl = models.IntegerField(default=0)
    blk = models.IntegerField(default=0)
    tov = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'games'

class Players(models.Model):
    player_id = models.IntegerField(primary_key=True)
    team_id = models.IntegerField(null=True)
    full_name = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    position = models.CharField(max_length=10, null=True)

    class Meta:
        managed = False
        db_table = 'players'

    def __str__(self):
        return self.player_id

class SeasonAverages(models.Model):
    player_id = models.IntegerField()
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
    
