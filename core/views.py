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




