from django.shortcuts import render
from django.views.generic.base import TemplateView


class TransactionPurposeList(TemplateView):
    template_name = "admin_panel/transaction-purpose/index.html"