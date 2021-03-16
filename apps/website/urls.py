"""
This is the URL module.
"""

__version__ = '0.1'
__author__ = 'Artem Yurchak'

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *


app_name = 'website'
urlpatterns = [
    path(
        '',
        IndexPage.as_view(),
        name='index'
    ),
    path(
        'about/',
        AboutPage.as_view(),
        name='about'
    ),
    path(
        'services/',
        ServicesPage.as_view(),
        name='services'
    ),
    path(
        'contacts/',
        ContactsPage.as_view(),
        name='contacts'
    ),
    path(
        'login/',
        LoginPage.as_view(),
        name='login'
    ),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
