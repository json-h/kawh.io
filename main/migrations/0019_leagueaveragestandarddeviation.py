# Generated by Django 3.1.4 on 2021-01-29 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_espnweekstatistics'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeagueAverageStandardDeviation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                'db_table': 'league_average_sd',
                'managed': False,
            },
        ),
    ]
