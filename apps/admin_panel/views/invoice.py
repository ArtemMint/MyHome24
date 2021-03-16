from django.shortcuts import render
from django.views.generic.base import TemplateView


class InvoiceList(TemplateView):
    template_name = "admin_panel/invoice/index.html"