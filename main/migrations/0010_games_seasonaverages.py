# Generated by Django 3.1.4 on 2020-12-29 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20201228_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=5)),
                ('game_id', models.CharField(max_length=15)),
                ('game_date', models.DateField(null=True)),
                ('home_id', models.IntegerField(default=0)),
                ('visitor_id', models.IntegerField(default=0)),
                ('mins', models.IntegerField(default=0)),
                ('fgm', models.IntegerField(default=0)),
                ('fga', models.IntegerField(default=0)),
                ('fg3m', models.IntegerField(default=0)),
                ('fg3a', models.IntegerField(default=0)),
                ('ftm', models.IntegerField(default=0)),
                ('fta', models.IntegerField(default=0)),
                ('pts', models.IntegerField(default=0)),
                ('off_reb', models.IntegerField(default=0)),
                ('def_reb', models.IntegerField(default=0)),
                ('tot_reb', models.IntegerField(default=0)),
                ('ast', models.IntegerField(default=0)),
                ('stl', models.IntegerField(default=0)),
                ('blk', models.IntegerField(default=0)),
                ('tov', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'games',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SeasonAverages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gp', models.IntegerField()),
                ('mins', models.DecimalField(decimal_places=1, max_digits=4)),
                ('fgm', models.DecimalField(decimal_places=1, max_digits=4)),
                ('fga', models.DecimalField(decimal_places=1, max_digits=4)),
                ('fgpct', models.DecimalField(decimal_places=3, max_digits=4)),
                ('ftm', models.DecimalField(decimal_places=1, max_digits=4)),
                ('fta', models.DecimalField(decimal_places=1, max_digits=4)),
                ('ftpct', models.DecimalField(decimal_places=3, max_digits=4)),
                ('fg3m', models.DecimalField(decimal_places=1, max_digits=4)),
                ('pts', models.DecimalField(decimal_places=1, max_digits=4)),
                ('reb', models.DecimalField(decimal_places=1, max_digits=4)),
                ('ast', models.DecimalField(decimal_places=1, max_digits=4)),
                ('stl', models.DecimalField(decimal_places=1, max_digits=4)),
                ('blk', models.DecimalField(decimal_places=1, max_digits=4)),
                ('tov', models.DecimalField(decimal_places=1, max_digits=4)),
            ],
            options={
                'db_table': 'season_averages_9cat',
                'managed': False,
            },
        ),
    ]
