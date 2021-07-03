from rest_framework import views, generics
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from register import models
from rest_api import serializers


class UserRoleView(views.APIView):
    model = models.User

    def get(self, request):
        user = get_object_or_404(self.model, pk=request.GET.get('pk'))
        try:
            role = user.role
        except AttributeError:
            role = 'Без роли'
        return Response({'role': role})


class UserDataView(generics.ListAPIView):
    model = models.User
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        flat = self.request.query_params.get('flat')
        if flat:
            queryset = self.model.objects.filter(flats=flat)
        else:
            queryset = []
        return queryset
