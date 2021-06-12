from rest_framework import generics

from rest_api import serializers
from apps.admin_panel import models


class HouseList(generics.ListAPIView):
    model = models.House
    serializer_class = serializers.HouseSerializer
    queryset = models.House.get_houses_list()