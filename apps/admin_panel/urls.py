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
        views.AccountTransactionsListView.as_view(),
        name='account_transactions_list'
    ),
    path(
        'account-transaction/create-in',
        views.AccountTransactionsCreateInView.as_view(),
        name='account_transaction_create_in'
    ),
    path(
        'account-transaction/create-out',
        views.AccountTransactionsCreateOutView.as_view(),
        name='account_transaction_create_out'
    ),
    path(
        'account-transaction/update/<int:pk>',
        views.AccountTransactionsUpdateView.as_view(),
        name='account_transaction_update'
    ),
    path(
        'account-transaction/detail/<int:pk>',
        views.AccountTransactionsDetailView.as_view(),
        name='account_transaction_detail'
    ),
    path(
        'account-transaction/delete/<int:pk>',
        views.AccountTransactionsDeleteView.as_view(),
        name='account_transaction_delete'
    ),

    # Invoice
    path(
        'invoice/index/',
        views.InvoiceList.as_view(),
        name='invoice_list'
    ),
    path(
        'invoice/create/',
        views.InvoiceCreate.as_view(),
        name='invoice_create'
    ),
    path(
        'invoice/update/<int:pk>',
        views.InvoiceUpdate.as_view(),
        name='invoice_update'
    ),
    path(
        'invoice/detail/<int:pk>',
        views.InvoiceDetail.as_view(),
        name='invoice_detail'
    ),
    path(
        'invoice/delete/<int:pk>',
        views.InvoiceDelete.as_view(),
        name='invoice_delete'
    ),

    # Account
    path(
        'account/index/',
        views.AccountsListView.as_view(),
        name='accounts_list'
    ),
    path(
      'account/create/',
      views.AccountCreateView.as_view(),
      name='account_create'
    ),
    path(
      'account/update/<int:pk>',
      views.AccountUpdateView.as_view(),
      name='account_update'
    ),
    path(
      'account/detail/<int:pk>',
      views.AccountDetailView.as_view(),
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
        views.FlatsListView.as_view(),
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
        views.HouseListView.as_view(),
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
        views.MessageListView.as_view(),
        name='message_list'
    ),
    path(
        'message/create/',
        views.message_create_view,
        name='message_create'
    ),
    path(
        'message/detail/<int:pk>/',
        views.MessageDetailView.as_view(),
        name='message_detail'
    ),
    # path(
    #     'message/delete/<int:pk>/',
    #     views.MessageDeleteView.as_view(),
    #     name='message_delete'
    # ),

    # Master requests
    path(
        'master-request/index/',
        views.MasterRequestList.as_view(),
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
        'counter-data/counter_list/flat_pk=<int:flat_pk>',
        views.CounterListView.as_view(),
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
    path(
        'counter-data/delete/<int:pk>/',
        views.CounterDeleteView.as_view(),
        name='counter_delete'
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
        'role/',
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
        'pay-company/index/',
        views.PayCompany.as_view(),
        name='pay-company'
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
        'website/services/',
        views.ServicesSettings.as_view(),
        name='services'
    ),
    path(
        'website/contacts/',
        views.ContactsSettings.as_view(),
        name='contacts'
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
