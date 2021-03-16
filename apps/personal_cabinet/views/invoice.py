from django.shortcuts import render
from django.views.generic.base import TemplateView


class InvoiceList(TemplateView):
    template_name = "personal_cabinet/invoice/index.html"
