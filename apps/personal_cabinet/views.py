from django.shortcuts import render
from django.views.generic.base import TemplateView


class Statistics(TemplateView):
    template_name = "personal_cabinet/statistics.html"
