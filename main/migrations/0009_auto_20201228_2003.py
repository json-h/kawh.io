# Generated by Django 3.1.4 on 2020-12-29 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_seasonaverages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='player',
        ),
        migrations.DeleteModel(
            name='SeasonAverages',
        ),
        migrations.DeleteModel(
            name='Games',
        ),
    ]
