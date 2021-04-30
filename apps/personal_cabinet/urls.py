"""
This is the personal cabinet URL module.
"""

__version__ = '0.1'
__author__ = 'Artem Yurchak'

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from personal_cabinet.views.summary import *
from personal_cabinet.views.invoice import *
from personal_cabinet.views.master_request import *
from personal_cabinet.views.message import *
from personal_cabinet.views.tariff import *
from register import views


app_name = 'personal_cabinet'
urlpatterns = [

    # User login
    path(
        'site/login',
        views.UserLoginView.as_view(),
        name='user_login'
    ),

    # User logout
    path(
        'site/logout',
        LogoutView.as_view(next_page='personal_cabinet:user_login'),
        name='user_logout'
    ),

    # User register
    path(
        'site/register',
        views.UserRegisterView.as_view(),
        name='user_register'
    ),

    # Summary
    path(
        '',
        SummaryById.as_view(),
        name='summary'
    ),
    
    # Invoice
    path(
        'invoice/index/',
        InvoiceList.as_view(),
        name='invoice_list'
    ),

    # Messages
    path(
        'message/index/',
        MessagesList.as_view(),
        name='message_list'
    ),

    # Tariff
    path(
        'tariff/index/',
        TariffList.as_view(),
        name='tariff_list'
    ),

    # Master request
    path(
        'master-request/index/',
        MasterRequestList.as_view(),
        name='master_request_list'
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
