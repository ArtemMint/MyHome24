from rest_framework import serializers

from admin_panel import models
from rest_api import serializers as house_serializers
from rest_api import serializers as user_serializers


class FlatSerializer(serializers.ModelSerializer):
    # owner = user_serializers.UserSerializer()
    # house = house_serializers.HouseSerializer()

    class Meta:
        model = models.Flat
        fields = (
            'id',
            'number',
            'area',
            'tariff',
            'owner',
            'house',
        )
