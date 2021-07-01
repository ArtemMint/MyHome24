from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from admin_panel import models, forms, utils, custom_views


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class InvoiceList(custom_views.ListFilteringView):
    model = models.Invoice
    search_form = forms.InvoiceFilterForm
    template_name = "admin_panel/invoice/index.html"

    def get_context_data(self):
        context = super(InvoiceList, self).get_context_data()
        statistic = utils.get_short_statistic()
        context.update(statistic)
        return context


#TODO add invoice services to each views
@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class InvoiceCreate(generic.View, ):
    model = models.Invoice
    form_class = forms.InvoiceForm
    template_name = 'admin_panel/invoice/create.html'

    def get(self, request):
        form = self.form_class(
            initial={
                'created_date': utils.get_current_date(),
                'start_date': utils.get_current_date(),
                'end_date': utils.get_current_date(),
                'number': utils.generate_number(self.model),
            }
        )
        return self.success_url(form)

    def post(self, request):
        form = self.form_class(
            request.POST,
        )
        if form.is_valid():
            form.save()
            messages.success(request, 'Квитанция сохранена!')
            return redirect('admin_panel:invoice_list')
        return self.success_url(form)

    def success_url(self, form):
        return render(
            self.request,
            self.template_name,
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
        return self.success_url(form)

    def post(self, request, pk):
        invoice = self.get_object(pk)
        form = self.form_class(
            request.POST,
            instance=invoice,
        )
        if form.is_valid():
            form.save()
            messages.success(request, 'Квитанция обновлена!')
            return redirect('admin_panel:invoice_list')
        return self.success_url(form)

    def success_url(self, form):
        return render(
            self.request,
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
