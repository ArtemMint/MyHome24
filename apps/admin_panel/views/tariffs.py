from django.shortcuts import render
from django.views.generic.base import TemplateView


class TariffsList(TemplateView):
    template_name = "admin_panel/tariffs/index.html"