from django.shortcuts import render
from django.views.generic.base import TemplateView


class MessagesList(TemplateView):
    template_name = "admin_panel/messages/index.html"