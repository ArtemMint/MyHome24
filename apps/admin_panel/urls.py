"""
This is the admin URL module.
"""

__version__ = '0.1'
__author__ = 'Artem Yurchak'

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views.statistics import *
from .views.manage_site import *
from .views.account_transaction import *
from .views.invoice import *
from .views.personal_account import *
from .views.flats import *
from .views.users import *
from .views.master_request import *
from .views.messages import *
from .views.meter_readings import *
from .views.pay_company import *
from .views.roles import *
from .views.services import *
from .views.tariffs import *
from .views.transaction_purpose import *
from .views.users_admin import *
from .views.houses import *


app_name = 'admin_panel'
urlpatterns = [
    # Statistics
    path(
        '',
        Statistics.as_view(),
        name='statistics'
    ),
    
    # Cash register
    path(
        'account-transaction/index/',
        AccountTransactionList.as_view(),
        name='account_transaction_list'
    ),
    
    
    # Invoice
    path(
        'invoice/index/',
        InvoiceList.as_view(),
        name='invoice_list'
    ),
    
    # Personal account
    path(
        'account/index/',
        PersonalAccountList.as_view(),
        name='account_list'
    ),
    
    # Flats
    path(
        'flat/index/',
        FlatsList.as_view(),
        name='flat_list'
    ),
    
    # Users
    path(
        'user/index/',
        UsersList.as_view(),
        name='user_list'
    ),
    
    # Houses
    path(
        'house/index/',
        HousesList.as_view(),
        name='house_list'
    ),
    
    # Messsages
    path(
        'message/index/',
        MessagesList.as_view(),
        name='message_list'
    ),
    
    # Master requests
    path(
        'master-request/index/',
        MasterRequestsList.as_view(),
        name='master_request_list'
    ),
    
    # Meter readings
    path(
        'meter-readings/index/',
        MeterReadingsList.as_view(),
        name='meter_readings_list'
    ),
    
    # Services
    path(
        'service/index/',
        ServicesList.as_view(),
        name='service_list'
    ),
    
    # Tariffs
    path(
        'tariff/index/',
        TariffsList.as_view(),
        name='tariff_list'
    ),
    
    # Roles
    path(
        'user-admin/role/',
        RolesList.as_view(),
        name='role_list'
    ),
    
    # User admin
    path(
        'user-admin/index/',
        UsersAdminList.as_view(),
        name='user_admin_list'
    ),
    
    # Pay company
    path(
        'pay-company/index/',
        PayCompany.as_view(),
        name='pay_company'
    ),
    
    # Transaction-purpose
    path(
        'transaction-purpose/index/',
        TransactionPurposeList.as_view(),
        name='transaction_purpose_list'
    ),
    
    # Manage site
    path(
        'website/home/',
        HomeSettings.as_view(),
        name='home'
    ),
    path(
        'website/about/',
        AboutSettings.as_view(),
        name='about'
    ),
    path(
        'website/services/',
        ServicesSettings.as_view(),
        name='services'
    ),
    path(
        'website/tariffs/',
        TariffsSettings.as_view(),
        name='tariffs'
    ),
    path(
        'website/contacts/',
        ContactsSettings.as_view(),
        name='contacts'
    ),
    
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
