from django.shortcuts import render
from django.views.generic.base import TemplateView


class MessagesList(TemplateView):
    template_name = "personal_cabinet/messages/index.html"
