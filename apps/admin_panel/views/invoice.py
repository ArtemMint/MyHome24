from django.shortcuts import render
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class InvoiceList(generic.ListView):
    template_name = "admin_panel/invoice/index.html"


class InvoiceCreate(generic.CreateView):
    pass


class InvoiceUpdate(generic.UpdateView):
    pass


class InvoiceDetail(generic.DetailView):
    pass


class InvoiceDelete(generic.DeleteView):
    pass
