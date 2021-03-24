"""
View of account transitions of users
"""

# from django.shortcuts import render
from django.views.generic.base import TemplateView


class AccountTransactionList(TemplateView):
    """
    Accoun transaction list of all users
    """
    template_name = "admin_panel/account_transaction/index.html"
