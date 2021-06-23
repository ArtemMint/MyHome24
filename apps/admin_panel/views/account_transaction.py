"""
View of account transitions of users
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from admin_panel import models, forms, utils


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class AccountTransactionsList(generic.View):
    """
    AccountTransaction list of all users
    """
    model = models.AccountTransaction
    form_class = forms.AccountTransactionFilter
    template_name = 'admin_panel/account_transaction/index.html'

    def get(self, request):
        f = self.form_class(
            request.GET,
            queryset=self.model.get_queryset_list()
        )
        statistic = utils.get_short_statistic()
        context = {
            'filter': f,
            'total_income': models.AccountTransaction.get_total_income(),
            'total_expenditure': models.AccountTransaction.get_total_expenditure(),
        }
        context.update(statistic)
        return render(
            request,
            self.template_name,
            context,
        )


# class AccountTransactionFiltered(generic.View):
#     models


@login_required(login_url='/admin/site/login')
def account_transactions_create_in(request):
    account_transaction_form = forms.AccountTransactionIncomeForm(
        initial={
            'number': utils.generate_number(models.AccountTransaction),
            'created_date': utils.get_current_date(),
        }
    )
    if request.POST:
        account_transaction_form = forms.AccountTransactionIncomeForm(
            request.POST,
        )
        if account_transaction_form.is_valid():
            a_t = account_transaction_form.save(commit=False)
            a_t.type = 'Приход'
            a_t.save()
            messages.success(request, 'Приходная ведомость создан!')
            return redirect('admin_panel:account_transactions_list')
        else:
            messages.warning(request, 'Ошибка создания ведомости!')
    return render(
        request,
        'admin_panel/account_transaction/create_in.html',
        {
            'account_transaction_form': account_transaction_form,
        }
    )


def account_transactions_create_out(request):
    account_transaction_form = forms.AccountTransactionExpenditureForm(
        initial={
            'number': utils.generate_number(models.AccountTransaction),
            'created_date': utils.get_current_date(),
        }
    )
    if request.POST:
        account_transaction_form = forms.AccountTransactionExpenditureForm(
            request.POST,
        )
        if account_transaction_form.is_valid():
            a_t = account_transaction_form.save(commit=False)
            a_t.total = -a_t.total
            a_t.type = 'Расход'
            a_t.save()
            messages.success(request, 'Расходная ведомость создан!')
            return redirect('admin_panel:account_transactions_list')
        else:
            messages.warning(request, 'Ошибка создания ведомости!')
    return render(
        request,
        'admin_panel/account_transaction/create_out.html',
        {
            'account_transaction_form': account_transaction_form,
        }
    )


@login_required(login_url='/admin/site/login')
def account_transactions_update(request, pk):
    account_transaction = models.AccountTransaction.get_account_transaction_by_pk(pk=pk)
    if account_transaction.transaction.type == 'Приход':
        account_transaction_form = forms.AccountTransactionIncomeForm(
            instance=account_transaction,
        )
    else:
        account_transaction_form = forms.AccountTransactionExpenditureForm(
            instance=account_transaction,
        )
    if request.POST:
        if account_transaction.transaction.type == 'Приход':
            account_transaction_form = forms.AccountTransactionIncomeForm(
                request.POST,
                instance=account_transaction,
            )
        else:
            account_transaction_form = forms.AccountTransactionExpenditureForm(
                request.POST,
                instance=account_transaction,
            )
        if account_transaction_form.is_valid():
            account_transaction_form.save()
            messages.success(request, 'Ведомость обновлена!')
            return redirect('admin_panel:account_transactions_list')
        else:
            messages.warning(request, 'Ошибка обновления ведомости!')
    return render(
        request,
        'admin_panel/account_transaction/update.html',
        {
            'account_transaction_form': account_transaction_form,
        }
    )


@login_required(login_url='/admin/site/login')
def account_transactions_detail(request, pk):
    return render(
        request,
        'admin_panel/account_transaction/detail.html',
        {
            'account_transaction_data': models.AccountTransaction.get_account_transaction_by_pk(pk=pk),
        }
    )


@login_required(login_url='/admin/site/login')
def account_transactions_delete(request, pk):
    account_transaction = models.AccountTransaction.get_account_transaction_by_pk(pk=pk)
    if request.POST:
        account_transaction.delete()
        return redirect('admin_panel:account_transactions_list')
    return render(
        request,
        'admin_panel/account_transaction/delete.html',
        {
            'account_transaction_data': account_transaction,
        }
    )
