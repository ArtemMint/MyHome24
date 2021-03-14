from django.shortcuts import render
from django.views.generic.base import TemplateView


class Statistics(TemplateView):
    template_name = "admin_panel/statistics.html"