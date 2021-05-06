from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
)

from admin_panel.models.transaction_purpose import TransactionPurpose


class TransactionPurposeList(ListView):
    model = TransactionPurpose
    template_name = "admin_panel/transaction-purpose/index.html"