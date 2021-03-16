from django.shortcuts import render
from django.views.generic.base import TemplateView


class HousesList(TemplateView):
    template_name = "admin_panel/houses/index.html"