from django.shortcuts import render
from django.views.generic.base import TemplateView


class MasterRequestList(TemplateView):
    template_name = "personal_cabinet/master_request/index.html"
