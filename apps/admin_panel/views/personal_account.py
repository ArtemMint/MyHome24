from django.shortcuts import render
from django.views.generic.base import TemplateView


class PersonalAccountList(TemplateView):
    template_name = "admin_panel/personal_account/index.html"