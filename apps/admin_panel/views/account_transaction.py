from django.shortcuts import render
from django.views.generic.base import TemplateView


class AccountTransactionList(TemplateView):
    template_name = "admin_panel/account_transaction/index.html"