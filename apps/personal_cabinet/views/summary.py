from django.shortcuts import render
from django.views.generic.base import TemplateView


class SummaryById(TemplateView):
    template_name = "personal_cabinet/summary/index.html"
