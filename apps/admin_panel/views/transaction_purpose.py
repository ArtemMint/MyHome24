from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from admin_panel.models.transaction_purpose import \
    TransactionPurpose
from admin_panel.forms.transaction_purpose import \
    TransactionPurposeForm


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class TransactionPurposeList(ListView):
    model = TransactionPurpose
    context_object_name = 'transaction_purpose_list'
    template_name = 'admin_panel/transaction-purpose/index.html'


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class TransactionPurposeCreate(SuccessMessageMixin, CreateView):
    model = TransactionPurpose
    form_class = TransactionPurposeForm
    success_url = reverse_lazy('admin_panel:transaction_purpose_list')
    success_message = 'Все успешно сохранено!'
    template_name = 'admin_panel/transaction-purpose/create.html'


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class TransactionPurposeUpdate(SuccessMessageMixin, UpdateView):
    model = TransactionPurpose
    form_class = TransactionPurposeForm
    success_url = reverse_lazy('admin_panel:transaction_purpose_list')
    success_message = 'Все успешно сохранено!'
    template_name = 'admin_panel/transaction-purpose/update.html'


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class TransactionPurposeDelete(DeleteView):
    model = TransactionPurpose
    success_url = reverse_lazy('admin_panel:transaction_purpose_list')
    template_name = 'admin_panel/transaction-purpose/delete.html'
