"""
This is the admin URL module.
"""

__version__ = '0.1'
__author__ = 'Artem Yurchak'

from django.urls import path
from . import views

app_name = 'rest_api'
urlpatterns = [
    path('house/',
         views.HouseList.as_view(),
         name='houses_list'
    ),


]
