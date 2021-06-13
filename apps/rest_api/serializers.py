from rest_framework import serializers

from admin_panel import models
from register.models import User


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.House
        fields = (
            'id',
            'name',
        )


class HouseSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HouseSection
        fields = (
            'id',
            'house',
            'name',
        )


class HouseFloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HouseFloor
        fields = (
            'id',
            'house',
            'name',
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'phone_number',
        )


class FlatSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    house = HouseSerializer(read_only=True)

    class Meta:
        model = models.Flat
        fields = (
            'id',
            'number',
            'owner',
            'house',
        )
