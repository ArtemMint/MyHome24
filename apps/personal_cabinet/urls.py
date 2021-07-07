"""
This is the personal cabinet URL module.
"""

__version__ = '0.1'
__author__ = 'Artem Yurchak'

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from personal_cabinet import views
from register import views as reg_views


app_name = 'personal_cabinet'
urlpatterns = [
    # User login
    path(
        'site/login',
        reg_views.UserLoginView.as_view(),
        name='user_login'
    ),

    # User logout
    path(
        'site/logout',
        LogoutView.as_view(next_page='personal_cabinet:user_login'),
        name='user_logout'
    ),

    # Summary
    path(
        '',
        views.SummaryById.as_view(),
        name='summary'
    ),
    
    # Invoice
    path(
        'invoice/index/',
        views.InvoiceList.as_view(),
        name='invoice_list'
    ),

    # Messages
    path(
        'message/index/',
        views.MessagesList.as_view(),
        name='message_list'
    ),

    # Tariff
    path(
        'tariff/index/',
        views.TariffList.as_view(),
        name='tariff_list'
    ),

    # Master request
    path(
        'master-request/index/',
        views.MasterRequestListView.as_view(),
        name='master_request_list'
    ),
    path(
        'master-request/delete/<int:pk>',
        views.MasterRequestDeleteView.as_view(),
        name='master_request_delete'
    ),

    # User profile
    path(
        'user/view/',
        views.UserProfileView.as_view(),
        name='user_profile'
    ),
    path(
        'user/update/',
        views.UpdateUserProfileView.as_view(),
        name='user_update'
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
