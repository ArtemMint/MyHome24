from django.shortcuts import render
from django.views.generic.base import TemplateView


class ServicesList(TemplateView):
    template_name = "admin_panel/services/index.html"