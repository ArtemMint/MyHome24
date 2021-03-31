"""
Website views
"""

from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from admin_panel import models


class IndexPage(DetailView):
    """
    Index page views
    """
    context_object_name = 'index_page'
    template_name = 'website/index.html'

    def get_object(self, queryset=None):
        """
        Get index page data
        """
        return models.IndexPage.get_solo()

    def get_context_data(self, **kwargs):
        """
        Get context data for index page
        """
        context = super(IndexPage, self).get_context_data(**kwargs)
        context['contacts_address'] = models.ContactsAddress.objects.last()
        return context


class AboutPage(DetailView):
    context_object_name = 'about_page'
    template_name = "website/about.html"

    def get_object(self, queryset=None):
        """
        Get contacts page data
        """
        return models.AboutPage.get_solo()

    def get_context_data(self, **kwargs):
        """
        Get context data for contacts page
        """
        context = super(AboutPage, self).get_context_data(**kwargs)
        context['about_gallery'] = models.AboutGallery.objects.all()
        context['about_extra_info'] = models.AboutExtraInfo.objects.last()
        context['about_extra_gallery'] = models.AboutExtraGallery.objects.all()
        context['about_documents'] = models.AboutDocument.objects.all()
        return context


class ServicesPage(DetailView):
    context_object_name = 'services_page'
    template_name = "website/services.html"

    def get_object(self, queryset=None):
        """
        Get contacts page data
        """
        return models.ServicesPage.get_solo()


class ContactsPage(DetailView):
    context_object_name = 'contacts_page'
    template_name = "website/contacts.html"

    def get_object(self, queryset=None):
        """
        Get contacts page data
        """
        return models.ContactsPage.get_solo()

    def get_context_data(self, **kwargs):
        """
        Get context data for contacts page
        """
        context = super(ContactsPage, self).get_context_data(**kwargs)
        context['contacts_map'] = models.ContactsMap.objects.last()
        context['contacts_address'] = models.ContactsAddress.objects.last()
        return context


class LoginPage(TemplateView):
    template_name = "website/login.html"
