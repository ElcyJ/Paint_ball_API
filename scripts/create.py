from core.models import *
map = Map(width=300, height=300)
map.save()
team = Team(color='A', quant_players=3, map=map)
team.save()
gun = Gun(number=1, ammunition=100, range=5)
gun.save()
player = Player(name='ana', password='123', localization_x=45, localization_y=150, team=team, gun=gun)
player.save()