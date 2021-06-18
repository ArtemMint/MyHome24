from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

from rest_api import serializers
from apps.admin_panel import models


class HouseList(generics.ListAPIView):
    model = models.House
    queryset = models.House.get_houses_list()
    serializer_class = serializers.HouseSerializer


class HouseCreate(generics.CreateAPIView):
    model = models.House
    serializer_class = serializers.HouseSerializer


class HouseUpdate(views.APIView):
    model = models.House
    serializer_class = serializers.HouseSerializer

    def get_object(self, pk):
        try:
            return self.model.get_house_by_pk(pk=pk)
        except self.model.DoesNotExist:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request, pk):
        house = self.get_object(pk)
        serializeobj = self.serializer_class(house)
        return Response(serializeobj.data)

    def put(self, request, pk):
        house = self.get_object(pk)
        houseserialize = self.serializer_class(
            house,
            data=request.data,
        )
        if houseserialize.is_valid():
            houseserialize.save()
            return Response(
                houseserialize.data,
                status=status.HTTP_200_OK
            )
        return Response(
            houseserialize.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class HouseDelete(generics.DestroyAPIView):
    model = models.House
    serializer_class = serializers.HouseSerializer

    def get_object(self, pk):
        try:
            return self.model.get_house_by_pk(pk=pk)
        except self.model.DoesNotExist:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request, pk):
        house = self.get_object(pk)
        serializeobj = self.serializer_class(house)
        return Response(serializeobj.data)

    def delete(self, request, pk):
        house = self.get_object(pk)
        house.delete()
        return Response(
            status=status.HTTP_200_OK
        )
