"""
View of account transitions of users
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from admin_panel import models, forms, utils, custom_views


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class AccountTransactionsListView(custom_views.ListFilteringView):
    """
    AccountTransaction list of all users
    """
    model = models.AccountTransaction
    search_form = forms.AccountTransactionFilter
    template_name = 'admin_panel/account_transaction/index.html'

    def get_context_data(self):
        statistic = utils.get_short_statistic()
        context = super(AccountTransactionsListView, self).get_context_data()
        context.update({
            'total_income': models.AccountTransaction.get_total_income(),
            'total_expenditure': models.AccountTransaction.get_total_expenditure(),
        })
        context.update(statistic)
        return context


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class AccountTransactionsCreateInView(generic.View):
    model = models.AccountTransaction
    form_class = forms.AccountTransactionIncomeForm
    template_name = 'admin_panel/account_transaction/create_in.html'

    def get(self, request):
        form = self.form_class(
            initial={
                'number': utils.generate_number(models.AccountTransaction),
                'created_date': utils.get_current_date(),
            }
        )
        return self.render_to_response(form)

    def post(self, request):
        form = self.form_class(
            self.request.POST,
        )
        if form.is_valid():
            a_t = form.save(commit=False)
            a_t.type = 'Приход'
            a_t.save()
            messages.success(self.request, 'Приходная ведомость создан!')
            return redirect('admin_panel:account_transactions_list')
        else:
            messages.warning(self.request, 'Ошибка создания ведомости!')
        return self.render_to_response(form)

    def render_to_response(self, form):
        return render(
            self.request,
            self.template_name,
            {
                'account_transaction_form': form,
            }
        )


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class AccountTransactionsCreateOutView(generic.View):
    model = models.AccountTransaction
    form_class = forms.AccountTransactionExpenditureForm
    template_name = 'admin_panel/account_transaction/create_out.html'

    def get(self, request):
        form = self.form_class(
            initial={
                'number': utils.generate_number(models.AccountTransaction),
                'created_date': utils.get_current_date(),
            }
        )
        return self.render_to_response(form)

    def post(self, request):
        form = forms.AccountTransactionExpenditureForm(
            self.request.POST,
        )
        if form.is_valid():
            a_t = form.save(commit=False)
            a_t.total = -a_t.total
            a_t.type = 'Расход'
            a_t.save()
            messages.success(self.request, 'Расходная ведомость создан!')
            return redirect('admin_panel:account_transactions_list')
        else:
            messages.warning(self.request, 'Ошибка создания ведомости!')
        return self.render_to_response(form)

    def render_to_response(self, form):
        return render(
            self.request,
            self.template_name,
            {
                'account_transaction_form': form,
            }
        )


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class AccountTransactionsUpdateView(generic.View):
    model = models.AccountTransaction
    form_in = forms.AccountTransactionIncomeForm
    form_out = forms.AccountTransactionExpenditureForm
    template_name = 'admin_panel/account_transaction/update.html'

    def get_object(self, pk):
        try:
            obj = self.model.get_account_transaction_by_pk(pk=pk)
        except self.model.DoesNotExist:
            obj = None
        return obj

    def get(self, request, pk: int):
        obj = self.get_object(pk)
        if obj.transaction.type == 'Приход':
            form = self.form_in(
                instance=obj,
            )
        else:
            form = self.form_out(
                instance=obj,
            )
        return self.render_to_response(form)

    def post(self, request, pk: int):
        obj = self.get_object(pk=pk)
        if obj.transaction.type == 'Приход':
            form = forms.AccountTransactionIncomeForm(
                self.request.POST,
                instance=obj,
            )
        else:
            form = forms.AccountTransactionExpenditureForm(
                self.request.POST,
                instance=obj,
            )
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Ведомость обновлена!')
            return redirect('admin_panel:account_transactions_list')
        else:
            messages.warning(self.request, 'Ошибка обновления ведомости!')
        return self.render_to_response(form)

    def render_to_response(self, form):
        return render(
            self.request,
            self.template_name,
            {
                'account_transaction_form': form,
            }
        )


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class AccountTransactionsDetailView(generic.DetailView):
    model = models.AccountTransaction
    context_object_name = 'account_transaction_data'
    template_name = 'admin_panel/account_transaction/detail.html'


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class AccountTransactionsDeleteView(generic.DeleteView):
    model = models.AccountTransaction
    context_object_name = 'account_transaction_data'
    template_name = 'admin_panel/account_transaction/delete.html'
    success_url = 'admin_panel:account_transactions_list'
