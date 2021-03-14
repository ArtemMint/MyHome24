from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexPage(TemplateView):
    template_name = "web_site/index.html"


class AboutPage(TemplateView):
    template_name = "web_site/about.html"


class ServicesPage(TemplateView):
    template_name = "web_site/services.html"


class ContactsPage(TemplateView):
    template_name = "web_site/contacts.html"


class LoginPage(TemplateView):
    template_name = "web_site/login.html"
