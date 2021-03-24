"""
Views of site data
"""

# from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView
from django.views import View

from .. import models
from .. import forms


class IndexUpdate(SuccessMessageMixin, View):
    """
    Index page view class
    """
    template_name = 'admin_panel/manage_site/index.html'

    def get_object(self):
        """
        Get index page data
        """
        obj = models.page_index.IndexPage.get_solo()
        return obj

    def get(self, request, *args, **kwargs):
        """
        GET method logic
        """
        index_page = self.get_object()
        index_form = forms.index.IndexPageForm(
            instance=index_page
        )
        slider_formset = forms.index.IndexSliderFormset(
            instance=index_page,
        )
        block_formset = forms.index.IndexBlockFormset(
            instance=index_page,
        )
        seo_form = forms.seo.SEOForm(
            instance=index_page.seo,
        )
        return render(
            request,
            self.template_name,
            {
                'index_page': index_page,
                'slider_formset': slider_formset,
                'index_form': index_form,
                'block_formset': block_formset,
                'seo_form': seo_form,
            }
        )

    def post(self, request, *args, **kwargs):
        """
        Post method logic
        """
        index_page = self.get_object()
        index_form = forms.index.IndexPageForm(
            request.POST,
            instance=index_page,
        )
        slider_formset = forms.index.IndexSliderFormset(
            request.POST,
            request.FILES,
            instance=index_page,
        )
        block_formset = forms.index.IndexBlockFormset(
            request.POST,
            request.FILES,
            instance=index_page,
        )
        seo_form = forms.seo.SEOForm(
            request.POST,
            instance=index_page.seo,
        )
        if (
                index_form.is_valid() and
                slider_formset.is_valid() and
                block_formset.is_valid() and
                seo_form.is_valid()
        ):
            index_form.save()
            slider_formset.save()
            block_formset.save()
            seo_form.save()
            return redirect('admin_panel:index')
        return render(
            request,
            self.template_name,
            {
                'index_page': index_page,
                'slider_formset': slider_formset,
                'index_form': index_form,
                'block_formset': block_formset,
                'seo_form': seo_form,
            }
        )


class AboutSettings(TemplateView):
    template_name = 'admin_panel/manage_site/about.html'

    def get_object(self):
        """
        Get about page data
        """
        obj = models.page_about.AboutPage.get_solo()
        return obj

    def get(self, request, *args, **kwargs):
        about_page: models = self.get_object()
        about_form: models = forms.about.AboutPageForm(
            instance=about_page,
        )
        gallery_formset = forms.about.AboutGalleryFormset(
            instance=about_page,
        )
        extra_info_form = forms.about.AboutExtraInfoForm(
            instance=about_page,
        )
        extra_gallery_formset = forms.about.AboutGalleryFormset(
            instance=about_page,
        )
        extra_document_formset = forms.about.AboutDocumentFormset(
            instance=about_page,
        )
        seo_form = forms.seo.SEOForm(
            instance=about_page.seo,
        )
        return render(
            request,
            self.template_name,
            {
                'about_page': about_page,
                'slider_formset': gallery_formset,
                'about_form': about_form,
                'extra_info_form': extra_info_form,
                'extra_gallery_formset': extra_gallery_formset,
                'extra_document_formset': extra_document_formset,
                'seo_form': seo_form,
            }
        )

    def post(self, request, *args, **kwargs):
        about_page: models.page_about = self.get_object()
        about_form: forms.about = forms.about.AboutPageForm(
            instance=about_page
        )
        gallery_formset = forms.about.AboutGalleryFormset(
            instance=about_page,
        )
        extra_info_form = forms.about.AboutExtraInfoForm(
            instance=about_page,
        )
        extra_gallery_formset = forms.about.AboutGalleryFormset(
            instance=about_page,
        )
        extra_document_formset = forms.about.AboutDocumentFormset(
            instance=about_page,
        )
        seo_form = forms.seo.SEOForm(
            instance=about_page.seo,
        )
        if (
                about_form.is_valid() and
                gallery_formset.is_valid() and
                extra_info_form.is_valid() and
                extra_gallery_formset.is_valid() and
                extra_document_formset.is_valid() and
                seo_form.is_valid()
         ):
            about_form.save()
            gallery_formset.save()
            extra_info_form.save()
            extra_gallery_formset.save()
            extra_document_formset.save()
            seo_form.save()
            return redirect('admin_panel:about')
        return render(
            request,
            self.template_name,
            {
                'about_page': about_page,
                'slider_formset': gallery_formset,
                'about_form': about_form,
                'extra_info_form': extra_info_form,
                'extra_gallery_formset': extra_gallery_formset,
                'extra_document_formset': extra_document_formset,
                'seo_form': seo_form,
            }
        )


class ServicesSettings(TemplateView):
    template_name = 'admin_panel/manage_site/services.html'


class TariffsSettings(TemplateView):
    template_name = 'admin_panel/manage_site/tariffs.html'


class ContactsSettings(TemplateView):
    template_name = 'admin_panel/manage_site/contacts.html'
