"""
This is the main URL module.
"""

__version__ = '0.1'
__author__ = 'Artem Yurchak'

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(
        'django_admin/',
        admin.site.urls
    ),
    path(
        'admin/',
        include('admin_panel.urls')
    ),
    path(
        'cabinet/',
        include('personal_cabinet.urls')
    ),
    path(
        'api/',
        include('rest_api.urls')
    ),
    path(
        '',
        include('website.urls')
    ),
]
