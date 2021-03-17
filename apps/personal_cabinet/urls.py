"""
This is the personal cabinet URL module.
"""

__version__ = '0.1'
__author__ = 'Artem Yurchak'

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views.summary import *
from .views.invoice import *
from .views.master_request import *
from .views.message import *
from .views.tariff import *
from .views.profile import *


app_name = 'personal_cabinet'
urlpatterns = [
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

    # Profile
    # path(
    #     '<int:flat_id>',
    #     SummaryById.as_view(),
    #     name='summary'
    # ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
