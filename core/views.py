from django.shortcuts import render
from .models import *
from rest_framework import viewsets, status
from .serializers import *


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
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
