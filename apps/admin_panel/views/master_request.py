from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

from admin_panel import models


@login_required(login_url='/admin/site/login')
def master_requests_list(request):
    return render(
        request,
        "admin_panel/master_request/index.html",
        {
            'master_requests_list': models.MasterRequest.get_queryset_list(),
        }
    )


@login_required(login_url='/admin/site/login')
def master_request_create(request):
    return render(
        request,
        "admin_panel/master_request/index.html",
        {
            'master_requests_list': models.MasterRequest.get_queryset_list(),
        }
    )


@login_required(login_url='/admin/site/login')
def master_request_update(request, pk):
    return render(
        request,
        "admin_panel/master_request/index.html",
        {
            'master_requests_list': models.MasterRequest.get_queryset_list(),
        }
    )


@login_required(login_url='/admin/site/login')
def master_request_detail(request, pk):
    return render(
        request,
        "admin_panel/master_request/index.html",
        {
            'master_requests_list': models.MasterRequest.get_queryset_list(),
        }
    )


@login_required(login_url='/admin/site/login')
def master_request_delete(request, pk):
    return render(
        request,
        "admin_panel/master_request/index.html",
        {
            'master_requests_list': models.MasterRequest.get_queryset_list(),
        }
    )
