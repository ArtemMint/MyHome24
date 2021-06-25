from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views import generic
from django.contrib.auth.decorators import login_required

from admin_panel import models, forms, utils


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class MasterRequestList(generic.View):
    model = models.MasterRequest
    form_class = forms.MasterRequestFilterForm
    template_name = 'admin_panel/master_request/index.html'

    def get(self, request):
        queryset = self.model.objects.all()
        master_request_number = self.model.get_all_queryset_count()
        f = self.form_class(
            request.GET,
            queryset=queryset,
        )
        return render(
            request,
            self.template_name,
            {
                'filter': f,
                'master_request_number': master_request_number,
            }
        )


@login_required(login_url='/admin/site/login')
def master_request_create(request):
    master_request_form = forms.MasterRequestForm(
        initial={
            'created_date': utils.get_current_date(),
        }
    )
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
    master_request_form = forms.MasterRequestForm(
        instance=models.MasterRequest.get_master_request_by_pk(pk=pk),
    )
    if request.POST:
        master_request_form = forms.MasterRequestForm(
            request.POST,
            instance=models.MasterRequest.get_master_request_by_pk(pk=pk),
        )
        if master_request_form.is_valid():
            master_request_form.save()
            messages.success(request, 'Заявка мастеру обновлена')
            return redirect('admin_panel:master_requests_list')
        else:
            messages.success(request, 'Ошибка обновления заявки!')
    return render(
        request,
        "admin_panel/master_request/update.html",
        {
            'master_request_form': master_request_form,
        }
    )


@login_required(login_url='/admin/site/login')
def master_request_detail(request, pk):
    return render(
        request,
        "admin_panel/master_request/detail.html",
        {
            'master_request_data': models.MasterRequest.get_master_request_by_pk(pk=pk),
        }
    )


@login_required(login_url='/admin/site/login')
def master_request_delete(request, pk):
    master_request_data = models.MasterRequest.get_master_request_by_pk(pk=pk)
    if request.POST:
        master_request_data.delete()
        return redirect('admin_panel:master_requests_list')
    return render(
        request,
        "admin_panel/master_request/delete.html",
        {
            'master_request_data': master_request_data,
        }
    )
