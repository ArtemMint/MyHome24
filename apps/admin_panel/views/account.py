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

        }
    )


@login_required(login_url='/admin/site/login')
def account_create(request):
    pass


@login_required(login_url='/admin/site/login')
def account_update(request):
    pass


@login_required(login_url='/admin/site/login')
def account_detail(request):
    pass


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class HouseDeleteView(generic.DeleteView):
    model = models.House
    success_url = reverse_lazy('admin_panel:houses_list')
    template_name = 'admin_panel/houses/delete.html'
