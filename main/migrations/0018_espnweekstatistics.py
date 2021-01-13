# Generated by Django 3.1.4 on 2021-01-13 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20201231_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='ESPNWeekStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField()),
                ('fgpct', models.DecimalField(decimal_places=3, max_digits=4)),
                ('ftpct', models.DecimalField(decimal_places=3, max_digits=4)),
                ('fg3m', models.IntegerField()),
                ('pts', models.IntegerField()),
                ('reb', models.IntegerField()),
                ('ast', models.IntegerField()),
                ('stl', models.IntegerField()),
                ('blk', models.IntegerField()),
                ('tov', models.IntegerField()),
            ],
            options={
                'db_table': 'week_statistics',
                'managed': False,
            },
        ),
    ]