from rest_framework import views
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from register import models


class UserRoleView(views.APIView):
    model = models.User

    def get(self, request):
        user = get_object_or_404(self.model, pk=request.GET.get('pk'))
        try:
            role = user.role
        except AttributeError:
            role = 'Без роли'
        return Response({'role': role})
