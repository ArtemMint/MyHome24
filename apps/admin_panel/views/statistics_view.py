from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

from admin_panel import models
from register import models as reg_models


@login_required(login_url='/cabinet/site/login')
def statistics_view(request):
    return render(
        request,
        'admin_panel/statistics/index.html',
        {
            'houses_number': models.House.get_houses_count(),
            'flats_number': models.Flat.get_flats_count(),
            'active_users_number': reg_models.User.get_active_users().count(),
            'accounts_number': models.Account.get_accounts_count(),
            'new_master_request_number': models.MasterRequest.get_new_request_count(),
            'in_work_master_request_number': models.MasterRequest.get_in_work_request_count(),
        }
    )
