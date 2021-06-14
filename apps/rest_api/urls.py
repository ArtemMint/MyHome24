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
         name='houses_list'),
    path('house/create/',
         views.HouseCreate.as_view(),
         name='house_create'),


    path('flat/',
         views.FlatList.as_view(),
         name='flats_list'),

]
