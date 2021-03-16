from django.shortcuts import render
from django.views.generic.base import TemplateView


class FlatsList(TemplateView):
    template_name = "admin_panel/flats/index.html"