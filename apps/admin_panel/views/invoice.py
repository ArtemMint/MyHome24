from django.shortcuts import render, redirect
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from admin_panel import models, forms, utils


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class InvoiceList(generic.View):
    model = models.Invoice
    template_name = "admin_panel/invoice/index.html"

    def get(self, request):
        queryset = self.model.get_invoice_list()
        statistic = utils.get_short_statistic()
        context = {
            'invoice_list': queryset,
        }
        context.update(statistic)
        return render(
            request,
            self.template_name,
            context,
        )


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
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
        return render(
            request,
            'admin_panel/invoice/create.html',
            {
                'form': form,
            }
        )


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class InvoiceUpdate(generic.View):
    model = models.Invoice
    form_class = forms.InvoiceForm

    def get_object(self, pk):
        return self.model.get_invoice_by_pk(pk)

    def get(self, request, pk):
        invoice = self.get_object(pk)
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

    def post(self, request, pk):
        invoice = self.get_object(pk)
        form = self.form_class(
            request.POST,
            instance=invoice,
        )
        if form.is_valid():
            form.save()
            return redirect('admin_panel:invoice_list')
        return render(
            request,
            'admin_panel/invoice/update.html',
            {
                'form': form,
            }
        )


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class InvoiceDetail(generic.View):
    model = models.Invoice
    form_class = forms.InvoiceForm

    def get(self, request, pk):
        invoice = self.model.get_invoice_by_pk(pk)
        return render(
            request,
            'admin_panel/invoice/detail.html',
            {
                'invoice': invoice
            }
        )


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class InvoiceDelete(generic.View):
    model = models.Invoice
    success_url = 'admin_panel:invoice_list'

    def get(self, request, pk):
        invoice = self.model.get_invoice_by_pk(pk)
        invoice.delete()
        return redirect(self.success_url)
