"""
View of account transitions of users
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from admin_panel import models
from admin_panel import forms


@login_required(login_url='/admin/site/login')
def account_transactions_list(request):
    """
    AccountTransaction list of all users
    """
    return render(
        request,
        'admin_panel/account_transaction/index.html',
        {
            'account_transactions_list': models.AccountTransaction.get_queryset_list(),
            'total_income': models.AccountTransaction.get_total_income(),
            'total_expenditure': models.AccountTransaction.get_total_expenditure(),
        }
    )


@login_required(login_url='/admin/site/login')
def account_transactions_create_in(request):
    account_transaction_form = forms.AccountTransactionIncomeForm()
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
            messages.success(request, 'Ошибка создания ведомости!')
    return render(
        request,
        'admin_panel/account_transaction/create_in.html',
        {
            'account_transaction_form': account_transaction_form,
        }
    )


def account_transactions_create_out(request):
    account_transaction_form = forms.AccountTransactionExpenditureForm()
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
            messages.success(request, 'Ошибка создания ведомости!')
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
    account_transaction_form = forms.AccountTransactionForm(
        instance=account_transaction,
    )
    if request.POST:
        account_transaction_form = forms.AccountTransactionForm(
            request.POST,
            instance=account_transaction,
        )
        if account_transaction_form.is_valid():
            account_transaction_form.save()
            messages.success(request, 'Ведомость обновлена!')
            return redirect('admin_panel:account_transactions_list')
        else:
            messages.success(request, 'Ошибка обновления ведомости!')
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
