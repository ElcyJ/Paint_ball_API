from core.models import *
map = Map(width=300, height=300)
map.save()
team = Team(color='A', quant_players=3, map=map)
team.save()
gun = Gun(number=1, ammunition=100, range=5)
gun.save()
player = Player(name='ana', localization_x=45, localization_y=150, team=team, gun=gun)
user = User.objects.create_user(username=player.name, email='player1@email.com', password=player.name+'1234')
user.save()
player.user = user
player.save()
shot = Shot(direction='U', player=Player.objects.get(name='ana'))
shot.save()