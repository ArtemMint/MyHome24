from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views import generic
from django.contrib.auth.decorators import login_required

from admin_panel import models


@login_required(login_url='/admin/site/login')
def accounts_list_view(request):
    return render(
        request,
        "admin_panel/account/index.html",
        {
            "accounts_list": models.Account.get_accounts_list(),
        }
    )


@login_required(login_url='/admin/site/login')
def account_create_view(request):
    return render(
        request,
        "admin_panel/account/create.html",
        {

        }
    )


@login_required(login_url='/admin/site/login')
def account_update_view(request):
    return render(
        request,
        "admin_panel/account/update.html",
        {

        }
    )


@login_required(login_url='/admin/site/login')
def account_detail_view(request):
    return render(
        request,
        "admin_panel/account/detail.html",
        {

        }
    )


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class AccountDeleteView(generic.DeleteView):
    model = models.Account
    success_url = reverse_lazy('admin_panel:accounts_list')
    template_name = 'admin_panel/account/delete.html'
