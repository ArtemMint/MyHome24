"""
This is the admin URL module.
"""

__version__ = '0.1'
__author__ = 'Artem Yurchak'

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from admin_panel.views import (
    statistics,
    account_transaction,
    personal_account,
    flats,
    houses,
    messages,
    users,
    users_admin,
    master_request,
    tariffs,
    roles,
    pay_company,
    meter_readings,
    manage_site,
    invoice,
    services,
    transaction_purpose,
)


app_name = 'admin_panel'
urlpatterns = [
    # Statistics
    path(
        '',
        statistics.Statistics.as_view(),
        name='statistics'
    ),
    
    # Cash register
    path(
        'account-transaction/index/',
        account_transaction.AccountTransactionList.as_view(),
        name='account_transaction_list'
    ),
    
    
    # Invoice
    path(
        'invoice/index/',
        invoice.InvoiceList.as_view(),
        name='invoice_list'
    ),
    
    # Personal account
    path(
        'account/index/',
        personal_account.PersonalAccountList.as_view(),
        name='account_list'
    ),
    
    # Flats
    path(
        'flat/index/',
        flats.FlatsList.as_view(),
        name='flat_list'
    ),
    
    # Users
    path(
        'user/index/',
        users.UsersList.as_view(),
        name='user_list'
    ),
    
    # Houses
    path(
        'house/index/',
        houses.HousesList.as_view(),
        name='house_list'
    ),
    
    # Messsages
    path(
        'message/index/',
        messages.MessagesList.as_view(),
        name='message_list'
    ),
    
    # Master requests
    path(
        'master-request/index/',
        master_request.MasterRequestsList.as_view(),
        name='master_request_list'
    ),
    
    # Meter readings
    path(
        'meter-readings/index/',
        meter_readings.MeterReadingsList.as_view(),
        name='meter_readings_list'
    ),
    
    # Services
    path(
        'service/index/',
        services.ServicesList.as_view(),
        name='service_list'
    ),
    
    # Tariffs
    path(
        'tariff/index/',
        tariffs.TariffsList.as_view(),
        name='tariff_list'
    ),
    
    # Roles
    path(
        'user-admin/role/',
        roles.RolesList.as_view(),
        name='role_list'
    ),
    
    # User admin
    path(
        'user-admin/index/',
        users_admin.UsersAdminList.as_view(),
        name='user_admin_list'
    ),
    
    # Pay company
    path(
        'pay-company/index/',
        pay_company.PayCompany.as_view(),
        name='pay_company'
    ),
    
    # Transaction-purpose
    path(
        'transaction-purpose/index/',
        transaction_purpose.TransactionPurposeList.as_view(),
        name='transaction_purpose_list'
    ),
    
    # Manage site
    path(
        'website/home/',
        manage_site.IndexUpdate.as_view(),
        name='index'
    ),
    path(
        'website/about/',
        manage_site.AboutSettings.as_view(),
        name='about'
    ),
    path(
        'website/services/',
        manage_site.ServicesSettings.as_view(),
        name='services'
    ),
    path(
        'website/contacts/',
        manage_site.ContactsSettings.as_view(),
        name='contacts'
    ),
    
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
