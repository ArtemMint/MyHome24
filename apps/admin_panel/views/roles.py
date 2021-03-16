from django.shortcuts import render
from django.views.generic.base import TemplateView


class RolesList(TemplateView):
    template_name = "admin_panel/roles/index.html"