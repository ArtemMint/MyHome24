from django.shortcuts import render, redirect
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from admin_panel import models
from admin_panel import forms
from admin_panel import utils


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class InvoiceList(generic.ListView):
    model = models.Invoice
    context_object_name = 'invoice_list'
    template_name = "admin_panel/invoice/index.html"


class InvoiceCreate(generic.View):
    model = models.Invoice
    form_class = forms.InvoiceForm

    def get(self, request):
        form = self.form_class(
            initial={
                'created_date': utils.get_current_date(),
                'start_date': utils.get_current_date(),
                'end_date': utils.get_current_date(),
                'number': utils.generate_number(self.model),
            }
        )
        return render(
            request,
            'admin_panel/invoice/create.html',
            {
                'form': form,
            }
        )

    def post(self, request):
        form = self.form_class(
            request.POST,
        )
        if form.is_valid():
            form.save()
            return redirect('admin_panel:invoice_list')


class InvoiceUpdate(generic.View):
    model = models.Invoice
    form_class = forms.InvoiceForm

    def get(self, request, pk):
        invoice = self.model.get_invoice_by_pk(pk)
        form = self.form_class(
                instance=invoice,
        )
        return render(
            request,
            'admin_panel/invoice/update.html',
            {
                'form': form,
            }
        )

    def post(self, request):
        form = self.form_class(
            request.POST,
        )
        if form.is_valid():
            form.save()
            return redirect('admin_panel:invoice_list')


class InvoiceDetail(generic.DetailView):
    pass


class InvoiceDelete(generic.DeleteView):
    pass
