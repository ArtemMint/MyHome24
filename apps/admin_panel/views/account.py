from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views import generic
from django.contrib.auth.decorators import login_required

from admin_panel import models, forms, utils, custom_views


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class AccountsListView(custom_views.ListFilteringView):
    model = models.Account
    search_form = forms.AccountFilter
    template_name = 'admin_panel/account/index.html'

    def get_context_data(self):
        context = super(AccountsListView, self).get_context_data()
        statistic = utils.get_short_statistic()
        context.update(statistic)
        return context


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class AccountCreateView(generic.View):
    model = models.Account
    form_class = forms.AccountForm
    template_name = 'admin_panel/account/create.html'

    def get(self, request):
        form = self.form_class(
            initial={
                'number': utils.generate_number(self.model),
            }
        )
        return self.success_url(form)

    def post(self, request):
        form = self.form_class(
            request.POST,
        )
        if form.is_valid():
            form.save()
            messages.success(request, 'Новый лицевой счет создан!')
            return redirect('admin_panel:accounts_list')
        return self.success_url(form)

    def success_url(self, form):
        return render(
            self.request,
            self.template_name,
            {
                'account_form': form,
            }
        )


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class AccountUpdateView(generic.View):
    model = models.Account
    form_class = forms.AccountForm
    template_name = "admin_panel/account/update.html"

    def get(self, request, pk):
        form = self.form_class(
            instance=self.model.get_account_by_pk(pk=pk),
        )
        return self.success_url(form)

    def post(self, request, pk):
        form = self.form_class(
            request.POST,
            instance=self.model.get_account_by_pk(pk=pk),
        )
        if form.is_valid():
            form.save()
            messages.success(request, 'Лицевой счет обновлен!')
            return redirect('admin_panel:accounts_list')
        return self.success_url(form)

    def success_url(self, form):
        return render(
            self.request,
            self.template_name,
            {
                'account_form': form,
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
