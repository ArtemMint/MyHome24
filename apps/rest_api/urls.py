"""
This is the admin URL module.
"""

__version__ = '0.1'
__author__ = 'Artem Yurchak'

from django.urls import path
from . import views

app_name = 'rest_api'
urlpatterns = [
    path(
        'overview/',
        views.ApiOverview.as_view(),
        name='api_overview',
    ),
    path(
        'statistic/',
        views.StatisticView.as_view(),
        name='api_statistic',
    ),
    path(
        'statistic/charts/',
        views.StatisticChartView.as_view(),
        name='api_chart_statistic',
    ),

    # User URLs.
    path(
        'user/role/',
        views.UserRoleView.as_view(),
        name='user_role',
    ),

    # House URLS.
    path(
        'house/list/',
        views.HouseList.as_view(),
        name='house_list',
    ),
    path(
        'house/create/',
        views.HouseCreate.as_view(),
        name='house_create',
    ),
    path(
        'house/update/<int:pk>',
        views.HouseUpdate.as_view(),
        name='house_update',
    ),
    path(
        'house/delete/<int:pk>',
        views.HouseDelete.as_view(),
        name='house_delete',
    ),

    # Flat URLS.
    path(
        'flat/list/',
        views.FlatList.as_view(),
        name='flat_list',
    ),
    path(
        'flat/create/',
        views.FlatCreate.as_view(),
        name='flat_create',
    ),
    path(
        'flat/update/<int:pk>',
        views.FlatUpdate.as_view(),
        name='flat_update',
    ),
    path(
        'flat/delete/<int:pk>',
        views.FlatDelete.as_view(),
        name='flat_delete',
    ),

    # Section
    path(
        'section/',
        views.SectionList.as_view(),
        name='section_list',
    ),

    # Floor
    path(
        'floor/',
        views.FloorList.as_view(),
        name='floor_list',
    ),

    # Flat
    path(
        'flat/',
        views.FlatQueryList.as_view(),
        name='flat_query_list',
    ),

]
