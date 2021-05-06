"""
This is the admin URL module.
"""

__version__ = '0.1'
__author__ = 'Artem Yurchak'

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from admin_panel import views
from register import views as register_views

app_name = 'admin_panel'
urlpatterns = [
    # Admin login
    path(
        'site/login',
        register_views.AdminLoginPage.as_view(),
        name='admin_login'
    ),

    # Statistics
    path(
        '',
        views.Statistics.as_view(),
        name='statistics'
    ),

    # Cash register
    path(
        'account-transaction/index/',
        views.AccountTransactionList.as_view(),
        name='account_transaction_list'
    ),


    # Invoice
    path(
        'invoice/index/',
        views.InvoiceList.as_view(),
        name='invoice_list'
    ),

    # Personal account
    path(
        'account/index/',
        views.PersonalAccountList.as_view(),
        name='account_list'
    ),

    # Flats
    path(
        'flat/index/',
        views.FlatsList.as_view(),
        name='flat_list'
    ),

    # Users
    path(
        'user/index/',
        views.UsersList.as_view(),
        name='user_list'
    ),

    # Houses
    path(
        'house/index/',
        views.HousesList.as_view(),
        name='house_list'
    ),

    # Messsages
    path(
        'message/index/',
        views.MessagesList.as_view(),
        name='message_list'
    ),

    # Master requests
    path(
        'master-request/index/',
        views.MasterRequestsList.as_view(),
        name='master_request_list'
    ),

    # Meter readings
    path(
        'meter-readings/index/',
        views.MeterReadingsList.as_view(),
        name='meter_readings_list'
    ),

    # Services
    path(
        'service/index/',
        views.ServicesList.as_view(),
        name='services_list'
    ),

    #Metrics
    path(
        'metrics/index/',
        views.MetricsList.as_view(),
        name='metrics_list'
    ),

    # Tariffs
    path(
        'tariff/index/',
        views.TariffList.as_view(),
        name='tariff_list'
    ),
    path(
        'tariff/create/',
        views.TariffCreate.as_view(),

        name='tariff_create'
    ),
    path(
        'tariff/detail/<int:pk>/',
        views.TariffDetail.as_view(),
        name='tariff_detail'
    ),
    path(
        'tariff/update/<int:pk>/',
        views.tariff_update_view,
        name='tariff_update'
    ),
    path(
        'tariff/copy/<int:pk>/',
        views.tariff_copy_view,
        name='tariff_copy'
    ),
    path(
        'tariff/delete/<int:pk>/',
        views.TariffDelete.as_view(),
        name='tariff_delete'
    ),

    # Roles
    path(
        'user-admin/role/',
        views.RolesList.as_view(),
        name='role_list'
    ),

    # User admin
    path(
        'user-admin/index/',
        views.UsersAdminList.as_view(),
        name='user_admin_list'
    ),

    # Pay company
    path(
        'pay_company/index/',
        views.PayCompany.as_view(),
        name='pay_company'
    ),

    # Transaction-purpose
    path(
        'transaction-purpose/index/',
        views.TransactionPurposeList.as_view(),
        name='transaction_purpose_list'
    ),

    # Manage site
    path(
        'website/home/',
        views.IndexSettings.as_view(),
        name='index'
    ),
    path(
        'website/about/',
        views.AboutSettings.as_view(),
        name='about'
    ),
    path(
        'website/services_metrics/',
        views.ServicesSettings.as_view(),
        name='services_metrics'
    ),
    path(
        'website/contacts/',
        views.ContactsSettings.as_view(),
        name='contacts'
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
