"""
This is the admin URL module.
"""

__version__ = '0.1'
__author__ = 'Artem Yurchak'

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LogoutView

from admin_panel import views
from register import views as register_views

app_name = 'admin_panel'
urlpatterns = [
    # Admin login
    path(
        'site/login',
        register_views.AdminLoginView.as_view(),
        name='admin_login'
    ),

    # Admin logout
    path(
        'site/logout',
        LogoutView.as_view(next_page='admin_panel:admin_login'),
        name='admin_logout'
    ),

    # Statistics
    path(
        '',
        views.statistics_view,
        name='statistics'
    ),

    # Cash register
    path(
        'account-transaction/index/',
        views.account_transactions_list,
        name='account_transactions_list'
    ),
    path(
        'account-transaction/create-in',
        views.account_transactions_create_in,
        name='account_transaction_create_in'
    ),
    path(
        'account-transaction/create-out',
        views.account_transactions_create_out,
        name='account_transaction_create_out'
    ),
    path(
        'account-transaction/update/<int:pk>',
        views.account_transactions_update,
        name='account_transaction_update'
    ),
    path(
        'account-transaction/detail/<int:pk>',
        views.account_transactions_detail,
        name='account_transaction_detail'
    ),
    path(
        'account-transaction/delete/<int:pk>',
        views.account_transactions_delete,
        name='account_transaction_delete'
    ),

    # Invoice
    path(
        'invoice/index/',
        views.InvoiceList.as_view(),
        name='invoice_list'
    ),

    # Account
    path(
        'account/index/',
        views.accounts_list_view,
        name='accounts_list'
    ),
    path(
      'account/create/',
      views.account_create_view,
      name='account_create'
    ),
    path(
      'account/update/<int:pk>',
      views.account_update_view,
      name='account_update'
    ),
    path(
      'account/detail/<int:pk>',
      views.account_detail_view,
      name='account_detail'
    ),
    path(
      'account/delete/<int:pk>',
      views.AccountDeleteView.as_view(),
      name='account_delete'
    ),

    # Flats
    path(
        'flat/index/',
        views.flats_list_view,
        name='flats_list'
    ),
    path(
      'flat/create/',
      views.flat_create_view,
      name='flat_create'
    ),
    path(
      'flat/update/<int:pk>',
      views.flat_update_view,
      name='flat_update'
    ),
    path(
      'flat/detail/<int:pk>',
      views.flat_detail_view,
      name='flat_detail'
    ),
    path(
      'flat/delete/<int:pk>',
      views.FlatDeleteView.as_view(),
      name='flat_delete'
    ),

    # Users
    path(
        'user/index/',
        views.users_list_view,
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
        views.houses_list_view,
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

    # Messages
    path(
        'message/index/',
        views.message_list_view,
        name='message_list'
    ),
    path(
        'message/create/',
        views.message_create_view,
        name='message_create'
    ),
    path(
        'message/detail/<int:pk>/',
        views.message_detail_view,
        name='message_detail'
    ),
    path(
        'message/delete/<int:pk>/',
        views.message_delete_view,
        name='message_delete'
    ),

    # Master requests
    path(
        'master-request/index/',
        views.master_requests_list,
        name='master_requests_list'
    ),
    path(
        'master-request/create/',
        views.master_request_create,
        name='master_request_create'
    ),
    path(
        'master-request/update/<int:pk>',
        views.master_request_update,
        name='master_request_update'
    ),
    path(
        'master-request/detail/<int:pk>',
        views.master_request_detail,
        name='master_request_detail'
    ),
    path(
        'master-request/delete/<int:pk>',
        views.master_request_delete,
        name='master_request_delete'
    ),

    # Counter data
    path(
        'counter-data/counters/',
        views.CountersView.as_view(),
        name='counters'
    ),
    path(
        'counter-data/counters_list?flat_pk=<int:flat_pk>',
        views.CountersListView.as_view(),
        name='counter_list'
    ),
    path(
        'counter-data/create/',
        views.CounterCreateView.as_view(),
        name='counter_create'
    ),
    path(
        'counter-data/update/<int:pk>/',
        views.CounterUpdateView.as_view(),
        name='counter_update'
    ),
    path(
        'counter-data/detail/<int:pk>/',
        views.CounterDetailView.as_view(),
        name='counter_detail'
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

    # User-admin
    path(
        'user-admin/index/',
        views.users_admin_list_view,
        name='users_admin_list'
    ),
    path(
        'user-admin/create/',
        views.user_admin_create_view,
        name='user_admin_create'
    ),
    path(
        'user-admin/update/<int:pk>',
        views.user_admin_update_view,
        name='user_admin_update'
    ),
    path(
        'user-admin/detail/<int:pk>',
        views.user_admin_detail_view,
        name='user_admin_detail'
    ),
    path(
        'user-admin/delete/<int:pk>',
        views.UserAdminDeleteView.as_view(),
        name='user_admin_delete'
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
