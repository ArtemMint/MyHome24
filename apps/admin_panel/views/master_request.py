from django.shortcuts import render
from django.views.generic.base import TemplateView


class MasterRequestsList(TemplateView):
    template_name = "admin_panel/master_request/index.html"