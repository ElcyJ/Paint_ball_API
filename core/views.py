from django.shortcuts import render
from .models import *
from .permissions import *
from rest_framework import viewsets, status
from .serializers import *
from rest_framework.response import Response


class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class GunViewSet(viewsets.ModelViewSet):
    queryset = Gun.objects.all()
    serializer_class = GunSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsUserOrReadyOnly]

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        player_instance = serializer.save()
        map_height = serializer['team']['map']['height'].value
        map_width = serializer['team']['map']['width'].value
        if request.data['localization_x'] <= map_width and request.data['localization_y'] <= map_height:
            self.perform_update(player_instance)
            return Response(serializer.data)

        return Response({'error': 'Out of map boundary!'},
                        status=status.HTTP_400_BAD_REQUEST)


class ShotViewSet(viewsets.ModelViewSet):
    queryset = Shot.objects.all()
    serializer_class = ShotSerializer

    def create(self, request, *args, **kwargs):
        shot_serializer = ShotSerializer(data=request.data)
        if shot_serializer.is_valid():
            player = Player.objects.get(name=request.data['player']['name'])
            other_players = Player.objects.all()

            if request.data['direction'] == 'D':
                shot_range = player.localization_y - player.gun.range
                for other_player in other_players:
                    if shot_range <= other_player.localization_y <= player.localization_y:
                        if player != other_player and player.team != other_player.team:
                            self.perform_create(shot_serializer)
                            Player.objects.get(name=other_player).delete()
                            return Response({'status': 'You hit a target!'})

            elif request.data['direction'] == 'U':
                shot_range = player.localization_y + player.gun.range
                for other_player in other_players:
                    if shot_range >= other_player.localization_y >= player.localization_y:
                        if player != other_player and player.team != other_player.team:
                            self.perform_create(shot_serializer)
                            Player.objects.get(name=other_player).delete()
                            return Response({'status': 'You hit a target!'})

            elif request.data['direction'] == 'R':
                shot_range = player.localization_x + player.gun.range
                for other_player in other_players:
                    if shot_range >= other_player.localization_y >= player.localization_y:
                        if player != other_player and player.team != other_player.team:
                            self.perform_create(shot_serializer)
                            Player.objects.get(name=other_player).delete()
                            return Response({'status': 'You hit a target!'})

            elif request.data['direction'] == 'L':
                shot_range = player.localization_x - player.gun.range
                for other_player in other_players:
                    if shot_range <= other_player.localization_y <= player.localization_y:
                        if player != other_player and player.team != other_player.team:
                            self.perform_create(shot_serializer)
                            Player.objects.get(name=other_player).delete()
                            return Response({'status': 'You hit a target!'})

            return Response({'status': 'You missed the target...'})


