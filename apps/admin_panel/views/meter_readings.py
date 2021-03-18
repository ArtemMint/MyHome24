from django.shortcuts import render
from django.views.generic.base import TemplateView


class MeterReadingsList(TemplateView):
    template_name = "admin_panel/meter_readings/index.html"
