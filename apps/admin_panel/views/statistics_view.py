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
            'houses_count': models.House.get_houses_count(),
            'flats_count': models.Flat.get_flats_count(),
            'active_users': reg_models.User.get_active_users().count(),
            'accounts_count': models.Account.get_accounts_count(),
        }
    )
