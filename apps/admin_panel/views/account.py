from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views import generic
from django.contrib.auth.decorators import login_required

from admin_panel import models, forms, utils


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class AccountsListView(generic.View):
    model = models.Account
    form_class = forms.AccountFilter
    template_name = 'admin_panel/account/index.html'

    def get(self, request):
        accounts_list = self.model.get_accounts_list()
        accounts_count = self.model.get_accounts_count()
        f = self.form_class(
            request.GET,
            queryset=accounts_list,
        )
        statistic = utils.get_short_statistic()
        context = {
            'filter': f,
            'accounts_count': accounts_count,
        }
        context.update(statistic)
        return render(
            request,
            self.template_name,
            context,
        )


@login_required(login_url='/admin/site/login')
def account_create_view(request):
    account_form = forms.AccountForm(
        initial={
            'number': utils.generate_number(models.AccountTransaction),
        }
    )
    if request.POST:
        account_form = forms.AccountForm(
            request.POST,
        )
        if account_form.is_valid():
            account_form.save()
            messages.success(request, 'Новый лицевой счет создан!')
            return redirect('admin_panel:accounts_list')
    return render(
        request,
        "admin_panel/account/create.html",
        {
            'account_form': account_form,
        }
    )


@login_required(login_url='/admin/site/login')
def account_update_view(request, pk):
    account_form = forms.AccountForm(
        instance=models.Account.get_account_by_pk(pk=pk),
    )
    if request.POST:
        account_form = forms.AccountForm(
            request.POST,
            instance=models.Account.get_account_by_pk(pk=pk),
        )
        if account_form.is_valid():
            account_form.save()
            messages.success(request, 'Лицевой счет обновлен!')
            return redirect('admin_panel:accounts_list')
    return render(
        request,
        "admin_panel/account/update.html",
        {
            'account_form': account_form,
        }
    )


@login_required(login_url='/admin/site/login')
def account_detail_view(request, pk):
    return render(
        request,
        "admin_panel/account/detail.html",
        {
            'account_data': models.Account.get_account_by_pk(pk=pk),
        }
    )


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class AccountDeleteView(generic.DeleteView):
    model = models.Account
    success_url = reverse_lazy('admin_panel:accounts_list')
    template_name = 'admin_panel/account/delete.html'
