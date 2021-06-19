from rest_framework import generics

from rest_api import serializers
from apps.admin_panel import models


class FlatList(generics.ListAPIView):
    serializer_class = serializers.FlatSerializer
    queryset = models.Flat.get_flats_list()


class FlatCreate(generics.CreateAPIView):
    pass


class FlatUpdate(generics.UpdateAPIView):
    pass


class FlatDelete(generics.DestroyAPIView):
    pass
