from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import generic

from admin_panel import models, forms


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class TransactionPurposeList(generic.ListView):
    model = models.TransactionPurpose
    context_object_name = 'transaction_purpose_list'
    template_name = 'admin_panel/transaction-purpose/index.html'


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class TransactionPurposeCreate(SuccessMessageMixin, generic.CreateView):
    model = models.TransactionPurpose
    form_class = forms.TransactionPurposeForm
    success_url = reverse_lazy('admin_panel:transaction_purpose_list')
    success_message = 'Все успешно сохранено!'
    template_name = 'admin_panel/transaction-purpose/create.html'


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class TransactionPurposeUpdate(SuccessMessageMixin, generic.UpdateView):
    model = models.TransactionPurpose
    form_class = forms.TransactionPurposeForm
    success_url = reverse_lazy('admin_panel:transaction_purpose_list')
    success_message = 'Все успешно сохранено!'
    template_name = 'admin_panel/transaction-purpose/update.html'


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class TransactionPurposeDelete(generic.DeleteView):
    model = models.TransactionPurpose
    success_url = reverse_lazy('admin_panel:transaction_purpose_list')
    template_name = 'admin_panel/transaction-purpose/delete.html'
