"""
View of account transitions of users
"""

from django.shortcuts import render, redirect
from django.views import generic
import datetime
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
        }
    )


@login_required(login_url='/admin/site/login')
def account_transactions_create(request):
    account_transaction_form = forms.AccountTransactionForm()
    if request.POST:
        account_transaction_form = forms.AccountTransactionForm(
            request.POST,
        )
        if account_transaction_form.is_valid():
            a_t = account_transaction_form.save(commit=False)
            a_t.type = 'Приход'
            a_t.save()
            messages.success(request, 'Новая ведомость создан!')
            return redirect('admin_panel:account_transactions_list')
    return render(
        request,
        'admin_panel/account_transaction/create.html',
        {
            'account_transaction_form': account_transaction_form,
        }
    )


@login_required(login_url='/admin/site/login')
def account_transactions_update(request):
    pass


@login_required(login_url='/admin/site/login')
def account_transactions_detail(request):
    pass


@login_required(login_url='/admin/site/login')
def account_transactions_delete(request):
    pass
