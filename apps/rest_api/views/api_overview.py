from rest_framework.response import Response
from rest_framework import views


class ApiOverview(views.APIView):

    def get(self, request):
        api_urls = {
            'House list': '/house/list/',
            'House create': '/house/create/',
            'House update': '/house/update/',
            'House delete': '/house/delete/',
            'Flat list': '/flat/list/',
            'Flat create': '/flat/create/',
            'Flat update': '/flat/update/',
            'Flat delete': '/flat/delete/',
        }
        return Response(api_urls)
