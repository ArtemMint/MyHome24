from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from rest_api import serializers
from apps.admin_panel import models


class FlatList(generics.ListAPIView):
    serializer_class = serializers.FlatSerializer
    queryset = models.Flat.get_flats_list()


class FlatCreate(generics.CreateAPIView):
    queryset = models.Flat.get_flats_list()
    serializer_class = serializers.FlatSerializer


class FlatUpdate(generics.RetrieveUpdateAPIView):
    model = models.Flat
    queryset = models.Flat.get_flats_list()
    serializer_class = serializers.FlatSerializer


class FlatDelete(generics.DestroyAPIView):
    queryset = models.Flat.get_flats_list()
    serializer_class = serializers.FlatSerializer

    def get(self, requst, pk):
        flat = self.get_object()
        flatserializer = self.serializer_class(flat)
        return Response(flatserializer.data)


class FlatQueryList(generics.ListAPIView):
    """
    Filter flat by House.
    """
    model = models.Flat
    serializer_class = serializers.FlatSerializer

    def get_queryset(self):
        section = self.request.query_params.get('section')
        if section:
            queryset = self.model.objects.filter(section=section)
        else:
            queryset = []
        return queryset
