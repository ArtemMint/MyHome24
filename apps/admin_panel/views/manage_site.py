from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomeSettings(TemplateView):
    template_name = "admin_panel/manage_site/home.html"

    
class AboutSettings(TemplateView):
    template_name = "admin_panel/manage_site/about.html"
    
    
class ServicesSettings(TemplateView):
    template_name = "admin_panel/manage_site/services.html"


class TariffsSettings(TemplateView):
    template_name = "admin_panel/manage_site/tariffs.html"
    
    
class ContactsSettings(TemplateView):
    template_name = "admin_panel/manage_site/contacts.html"