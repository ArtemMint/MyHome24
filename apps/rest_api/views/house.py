from rest_framework import generics

from rest_api import serializers
from apps.admin_panel import models


class HouseList(generics.ListAPIView):
    serializer_class = serializers.HouseSerializer
    queryset = models.House.get_houses_list()


class HouseCreate(generics.CreateAPIView):
    model = models.House
    http_method_names = ['post']
    serializer_class = serializers.HouseSerializer


