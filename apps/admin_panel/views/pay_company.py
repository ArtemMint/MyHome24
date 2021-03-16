from django.shortcuts import render
from django.views.generic.base import TemplateView


class PayCompany(TemplateView):
    template_name = "admin_panel/pay_company/index.html"