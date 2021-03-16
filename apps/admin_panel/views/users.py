from django.shortcuts import render
from django.views.generic.base import TemplateView


class UsersList(TemplateView):
    template_name = "admin_panel/users/index.html"