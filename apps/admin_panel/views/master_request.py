from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from admin_panel import models
from admin_panel import forms


@login_required(login_url='/admin/site/login')
def master_requests_list(request):
    return render(
        request,
        "admin_panel/master_request/index.html",
        {
            'master_requests_list': models.MasterRequest.get_all_queryset_list(),
        }
    )


@login_required(login_url='/admin/site/login')
def master_request_create(request):
    master_request_form = forms.MasterRequestForm()
    if request.POST:
        master_request_form = forms.MasterRequestForm(
            request.POST,
        )
        if master_request_form.is_valid():
            master_request_form.save()
            messages.success(request, 'Заявка мастеру создана!')
            return redirect('admin_panel:master_requests_list')
        else:
            messages.success(request, 'Ошибка создания заявки!')
    return render(
        request,
        "admin_panel/master_request/create.html",
        {
            'master_request_form': master_request_form,
        }
    )


@login_required(login_url='/admin/site/login')
def master_request_update(request, pk):
    return render(
        request,
        "admin_panel/master_request/index.html",
        {
            'master_requests_list': models.MasterRequest.get_all_queryset_list(),
        }
    )


@login_required(login_url='/admin/site/login')
def master_request_detail(request, pk):
    return render(
        request,
        "admin_panel/master_request/index.html",
        {
            'master_requests_list': models.MasterRequest.get_all_queryset_list(),
        }
    )


@login_required(login_url='/admin/site/login')
def master_request_delete(request, pk):
    return render(
        request,
        "admin_panel/master_request/index.html",
        {
            'master_requests_list': models.MasterRequest.get_all_queryset_list(),
        }
    )
