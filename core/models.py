from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Map(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()


class Team(models.Model):
    TEAM_COLORS = (
        ('A', 'Azul'),
        ('V', 'Vermelho'),
    )
    color = models.CharField(max_length=1, choices=TEAM_COLORS)
    quant_players = models.IntegerField()
    map = models.ForeignKey(Map, on_delete=models.CASCADE, related_name='teams')

    def __str__(self):
        return self.color


class Gun(models.Model):
    number = models.CharField(max_length=4)
    ammunition = models.IntegerField()
    range = models.IntegerField()


class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="player")
    name = models.CharField(max_length=255)
    localization_x = models.IntegerField()
    localization_y = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players_in_team")
    gun = models.ForeignKey(Gun, on_delete=models.CASCADE, related_name='players_with_gun')

    def __str__(self):
        return self.name + " - Team: " + self.team


class Shot(models.Model):
    DIRECTIONS_CHOICES = (
        ('U', 'UP'),
        ('D', 'Down'),
        ('R', 'Right'),
        ('L', 'Left'),
    )
    direction = models.CharField(max_length=1, choices=DIRECTIONS_CHOICES)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='shots')

