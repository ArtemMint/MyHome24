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


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class AccountCreateView(generic.View):
    model = models.Account
    form_class = forms.AccountForm
    template_name = 'admin_panel/account/create.html'

    def get(self, request):
        account_form = self.form_class(
            initial={
                'number': utils.generate_number(models.AccountTransaction),
            }
        )
        return render(
            request,
            self.template_name,
            {
                'account_form': account_form,
            }
        )

    def post(self, request):
        account_form = self.form_class(
            request.POST,
        )
        if account_form.is_valid():
            account_form.save()
            messages.success(request, 'Новый лицевой счет создан!')
            return redirect('admin_panel:accounts_list')
        return render(
            request,
            self.template_name,
            {
                'account_form': account_form,
            }
        )


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class AccountUpdateView(generic.View):
    model = models.Account
    form_class = forms.AccountForm
    template_name = "admin_panel/account/update.html"

    def get(self, request, pk):
        account_form = self.form_class(
            instance=self.model.get_account_by_pk(pk=pk),
        )
        return render(
            request,
            self.template_name,
            {
                'account_form': account_form,
            }
        )

    def post(self, request, pk):
        account_form = self.form_class(
            request.POST,
            instance=self.model.get_account_by_pk(pk=pk),
        )
        if account_form.is_valid():
            account_form.save()
            messages.success(request, 'Лицевой счет обновлен!')
            return redirect('admin_panel:accounts_list')
        return render(
            request,
            self.template_name,
            {
                'account_form': account_form,
            }
        )


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class AccountDetailView(generic.DetailView):
    model = models.Account
    context_object_name = 'account_data'
    template_name = "admin_panel/account/detail.html"


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class AccountDeleteView(generic.DeleteView):
    model = models.Account
    success_url = reverse_lazy('admin_panel:accounts_list')
    template_name = 'admin_panel/account/delete.html'
