from .models import *
from rest_framework import serializers


class MapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Map
        fields = ['url', 'width', 'height']


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    map = MapSerializer(many=False)

    class Meta:
        model = Team
        fields = ['url', 'color', 'quant_players', 'map']


class GunSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gun
        fields = ['url', 'number', 'ammunition', 'range']


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    team = TeamSerializer(many=False)
    gun = GunSerializer(many=False)

    class Meta:
        model = Player
        fields = ['url', 'name', 'password', 'localization_x', 'localization_y', 'team', 'gun']