from django.db import models

class LineupPlayer(models.Model):
    id = models.BigAutoField(primary_key=True)
    game_team = models.ForeignKey('GameTeam', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lineup_players'