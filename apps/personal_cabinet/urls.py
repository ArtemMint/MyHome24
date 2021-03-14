"""
This is the personal cabinet URL module.
"""

__version__ = '0.1'
__author__ = 'Artem Yurchak'

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *


app_name = 'personal_cabinet'
urlpatterns = [
    path(
        'statistics/',
        Statistics.as_view(),
        name='statistics'
    ),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
