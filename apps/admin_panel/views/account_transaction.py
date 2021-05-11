"""
View of account transitions of users
"""

# from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class AccountTransactionList(TemplateView):
    """
    Account transaction list of all users
    """
    template_name = "admin_panel/account_transaction/index.html"
