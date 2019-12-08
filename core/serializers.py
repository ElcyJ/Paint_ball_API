from .models import *
from rest_framework import serializers
from django.core.exceptions import ValidationError


class MapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Map
        fields = ['url', 'width', 'height']


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    map = MapSerializer(many=False)

    class Meta:
        model = Team
        fields = ['url', 'color', 'quant_players', 'map']

    def __init__(self, *args, **kwargs):
        super(TeamSerializer, self).__init__(*args, **kwargs)
        self.fields['quant_players'].required = False
        self.fields['map'].required = False

    def create(self, validated_data):
        team = Team(
            color=validated_data['color'],
            quant_players=validated_data['quant_players']
        )
        team.map = Map.objects.get(width=validated_data['map']['width'],
                                   height=validated_data['map']['height'])
        team.save()

        return team


class GunSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gun
        fields = ['url', 'number', 'ammunition', 'range']

    def __init__(self, *args, **kwargs):
        super(GunSerializer, self).__init__(*args, **kwargs)
        self.fields['ammunition'].required = False
        self.fields['range'].required = False


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    team = TeamSerializer(required=False)
    gun = GunSerializer(required=False)

    class Meta:
        model = Player
        fields = ['url', 'name', 'localization_x', 'localization_y', 'team', 'gun']
        extra_kwargs = {
            'name': {'read_only': True},
            'team': {'read_only': True},
            'gun': {'read_only': True}
        }

    def to_internal_value(self, data):
        team = data.get('team')
        gun = data.get('gun')
        if team and gun:
            data['team'] = {'color': team}
            data['gun'] = {'number': gun}
        ret = super(PlayerSerializer, self).to_internal_value(data)

        team = ret.get('team')
        gun = ret.get('gun')
        if team and gun:
            try:
                ret['team'] = Team.objects.get(color=team['color'])
                ret['gun'] = Gun.objects.get(number=gun['number'])
            except Team.DoesNotExist and Gun.DoesNotExist:
                raise ValidationError({'team': ['Team with the given color does not exist.'],
                                       'gun': ['Gun with the given number does not exist.']})
        return ret

    def create(self, validated_data):
        user = User(
            username=validated_data['name'],
            email=validated_data['name'] + "@email.com",
            password=validated_data['name'] + "1234"
        )
        user.save()
        player = Player(
            name=validated_data['name'],
            localization_x=validated_data['localization_x'],
            localization_y=validated_data['localization_y'],
            team=validated_data['team'],
            gun=validated_data['gun']
        )
        player.user = user
        player.save()

        return player



