from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required(login_url='/cabinet/site/login'), name='dispatch')
class Statistics(TemplateView):
    template_name = "admin_panel/statistics/index.html"
