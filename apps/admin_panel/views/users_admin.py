from django.shortcuts import render
from django.views.generic.base import TemplateView


class UsersAdminList(TemplateView):
    template_name = "admin_panel/users_admin/index.html"