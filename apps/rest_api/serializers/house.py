from rest_framework import serializers

from admin_panel import models


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.House
        fields = (
            'id',
            'name',
            'address',
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
