from django.shortcuts import render
from django.views.generic.base import TemplateView


class TariffList(TemplateView):
    template_name = "personal_cabinet/tariffs/index.html"
