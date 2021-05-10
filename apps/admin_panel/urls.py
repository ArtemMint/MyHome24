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
        views.UsersListView.as_view(),
        name='users_list'
    ),
    path(
      'user/create/',
      views.user_create_view,
      name='user_create'
    ),
    path(
      'user/update/<int:pk>',
      views.user_update_view,
      name='user_update'
    ),
    path(
      'user/detail/<int:pk>',
      views.user_detail_view,
      name='user_detail'
    ),
    path(
      'user/delete/<int:pk>',
      views.UserDeleteView.as_view(),
      name='user_delete'
    ),

    # Houses
    path(
        'house/index/',
        views.HousesListView.as_view(),
        name='houses_list'
    ),
    path(
        'house/create/',
        views.house_create_view,
        name='house_create'
    ),
    path(
        'house/update/<int:pk>',
        views.house_update_view,
        name='house_update'
    ),
    path(
        'house/detail/<int:pk>',
        views.house_detail_view,
        name='house_detail'
    ),
    path(
        'house/delete/<int:pk>',
        views.HouseDeleteView.as_view(),
        name='house_delete'
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
        views.service_update_view,
        name='services_list'
    ),

    # Metrics
    path(
        'metrics/index/',
        views.metrics_update_view,
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
        'tariff/detail/<int:pk>',
        views.TariffDetail.as_view(),
        name='tariff_detail'
    ),
    path(
        'tariff/update/<int:pk>',
        views.tariff_update_view,
        name='tariff_update'
    ),
    path(
        'tariff/copy/<int:pk>',
        views.tariff_copy_view,
        name='tariff_copy'
    ),
    path(
        'tariff/delete/<int:pk>',
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
    path(
        'transaction-purpose/create/',
        views.TransactionPurposeCreate.as_view(),
        name='transaction_purpose_create'
    ),
    path(
        'transaction-purpose/update/<int:pk>',
        views.TransactionPurposeUpdate.as_view(),
        name='transaction_purpose_update'
    ),
    path(
        'transaction-purpose/delete/<int:pk>',
        views.TransactionPurposeDelete.as_view(),
        name='transaction_purpose_delete'
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
