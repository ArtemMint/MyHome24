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
        obj = models.IndexPage.get_solo()
        if not obj.seo:
            obj.seo = models.SEO.objects.create()
        return obj

    def get(self, request, *args, **kwargs):
        """
        GET method logic
        """
        index_page = self.get_object()
        index_form = forms.IndexPageForm(
            instance=index_page
        )
        slider_formset = forms.IndexSliderFormset(
            instance=index_page,
        )
        block_formset = forms.IndexBlockFormset(
            instance=index_page,
        )
        seo_form = forms.SEOForm(
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
        index_form = forms.IndexPageForm(
            request.POST,
            instance=index_page,
        )
        slider_formset = forms.IndexSliderFormset(
            request.POST,
            request.FILES,
            instance=index_page,
        )
        block_formset = forms.IndexBlockFormset(
            request.POST,
            request.FILES,
            instance=index_page,
        )
        seo_form = forms.SEOForm(
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
        obj = models.AboutPage.get_solo()
        if not obj.seo:
            obj.seo = models.SEO.objects.create()
        return obj

    def get(self, request, *args, **kwargs):
        about_page: models.AboutPage = self.get_object()
        about_form = forms.AboutPageForm(
            instance=about_page,
        )
        gallery_formset = forms.AboutGalleryFormset(
            instance=about_page,
        )
        extra_info_formset = forms.AboutExtraInfoFormset(
            instance=about_page,
        )
        extra_gallery_formset = forms.AboutExtraGalleryFormset(
            instance=about_page,
        )
        extra_document_formset = forms.AboutDocumentFormset(
            instance=about_page,
        )
        seo_form = forms.SEOForm(
            instance=about_page.seo,
        )
        return render(
            request,
            self.template_name,
            {
                'about_page': about_page,
                'about_form': about_form,
                'gallery_formset': gallery_formset,
                'extra_info_formset': extra_info_formset,
                'extra_gallery_formset': extra_gallery_formset,
                'extra_document_formset': extra_document_formset,
                'documents': models.AboutDocument.objects.all(),
                'seo_form': seo_form,
            }
        )

    def post(self, request, *args, **kwargs):
        about_page = self.get_object()
        about_form = forms.AboutPageForm(
            request.POST,
            request.FILES,
            instance=about_page,
        )
        gallery_formset = forms.AboutGalleryFormset(
            request.POST,
            request.FILES,
            instance=about_page,
        )
        extra_info_formset = forms.AboutExtraInfoFormset(
            request.POST,
            instance=about_page,
        )
        extra_gallery_formset = forms.AboutExtraGalleryFormset(
            request.POST,
            request.FILES,
            instance=about_page,
        )
        document_formset = forms.AboutDocumentFormset(
            request.POST,
            request.FILES,
            instance=about_page,
        )
        seo_form = forms.SEOForm(
            request.POST,
            instance=about_page.seo,
        )
        if (
                about_form.is_valid() and
                gallery_formset.is_valid() and
                extra_info_formset.is_valid() and
                extra_gallery_formset.is_valid() and
                document_formset.is_valid() and
                seo_form.is_valid()
        ):
            about_form.save()
            gallery_formset.save()
            extra_info_formset.save()
            extra_gallery_formset.save()
            document_formset.save()
            seo_form.save()
            return redirect('admin_panel:about')
        return render(
            request,
            self.template_name,
            {
                'about_page': about_page,
                'about_form': about_form,
                'gallery_formset': gallery_formset,
                'extra_info_formset': extra_info_formset,
                'extra_gallery_formset': extra_gallery_formset,
                'extra_document_formset': document_formset,
                'documents': models.AboutDocument.objects.all(),
                'seo_form': seo_form,
            }
        )


class ServicesSettings(TemplateView):
    template_name = 'admin_panel/manage_site/services.html'


class TariffsSettings(TemplateView):
    template_name = 'admin_panel/manage_site/tariffs.html'


class ContactsSettings(TemplateView):
    template_name = 'admin_panel/manage_site/contacts.html'
