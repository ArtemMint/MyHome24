"""
Views of site data
"""

# from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView


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


class ServicesSettings(SuccessMessageMixin, UpdateView):
    """
    Services page settings
    """
    model = models.ServicesPage
    form_class = forms.ServicesForm
    formset_class = forms.ServicesFormset
    second_form_class = forms.SEOForm
    success_url = reverse_lazy('admin_panel:services')
    success_message = 'All services successfully updated!'
    template_name = 'admin_panel/manage_site/services.html'

    def __init__(self):
        super(ServicesSettings, self).__init__()
        self.object = self.get_object()

    def get_object(self, queryset=None):
        """
        Get services page data
        """
        obj = models.ServicesPage.get_solo()
        if not obj.seo:
            obj.seo = models.SEO.objects.create()
            obj.save()
        return obj

    def get_context_data(self, **kwargs):
        """
        Get context to render forms in page
        """
        context = super(ServicesSettings, self).get_context_data(**kwargs)
        context['services_formset'] = self.formset_class(
            instance=self.object,
        )
        context['seo_form'] = self.second_form_class(
            instance=self.object.seo,
        )
        return context

    def get(self, request, *args, **kwargs):
        """
        GET method
        """
        super(ServicesSettings, self).get(request, *args, **kwargs)
        return self.render_to_response(
            self.get_context_data(
                object=self.object,
                services_formset=self.formset_class,
                seo_form=self.second_form_class,
            )
        )

    def post(self, request, *args, **kwargs):
        """
        POST method
        """
        formset = self.formset_class(
            request.POST,
            request.FILES,
            instance=self.object,
        )
        form = self.second_form_class(
            request.POST,
            instance=self.object.seo,
        )
        if formset.is_valid() and form.is_valid():
            return self.forms_valid(
                formset,
                form,
            )
        else:
            return self.forms_invalid()

    def forms_valid(self, formset, form):
        """
        If form valid
        """
        formset.save()
        form.save()
        return super(ServicesSettings, self).form_valid(form)

    def forms_invalid(self):
        """
        If form invalid
        """
        return self.render_to_response(
            self.get_context_data(
                services_formset=self.formset_class,
                seo_form=self.second_form_class,
            )
        )


class ContactsSettings(SuccessMessageMixin, UpdateView):
    """
    Services page settings
    """
    model = models.ContactsPage
    form_class = forms.ContactsPageForm
    contacts_address_form_class = forms.ContactsAddressForm
    contacts_map_form_class = forms.ContactsMapForm
    seo_form_class = forms.SEOForm
    success_url = reverse_lazy('admin_panel:contacts')
    success_message = 'All contacts successfully updated!'
    template_name = 'admin_panel/manage_site/contacts.html'

    def __init__(self):
        super(ContactsSettings, self).__init__()
        self.object = self.get_object()

    def get_object(self, queryset=None):
        """
        Get contacts page data
        """
        obj = models.ContactsPage.get_solo()
        if not obj.seo:
            obj.seo = models.SEO.objects.create()
        if obj.map.count() == 0:
            obj.map.create()
        if obj.contacts_address.count() == 0:
            obj.contacts_address.create()
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        """
        Get context to render forms in page
        """
        context = super(ContactsSettings, self).get_context_data(**kwargs)
        context['contacts_page_form'] = self.form_class(
            instance=self.object,
        )
        context['contacts_address_form'] = self.contacts_address_form_class(
            instance=self.object.contacts_address.last(),
        )
        context['contacts_map_form'] = self.contacts_map_form_class(
            instance=self.object.map.last(),
        )
        context['seo_form'] = self.seo_form_class(
            instance=self.object.seo,
        )
        return context

    def get(self, request, *args, **kwargs):
        """
        GET method
        """
        super(ContactsSettings, self).get(request, *args, **kwargs)
        return self.render_to_response(
            self.get_context_data(
                object=self.object,
                contacts_page_form=self.form_class,
                contacts_address_form=self.contacts_address_form_class,
                contacts_map_form=self.contacts_map_form_class,
                seo_form=self.seo_form_class,
            )
        )

    def post(self, request, *args, **kwargs):
        """
        POST method
        """
        contacts_page_form = self.form_class(
            request.POST,
            instance=self.object,
        )
        contacts_address_form = self.contacts_address_form_class(
            request.POST,
            instance=self.object.contacts_address.last(),
        )
        contacts_map_form = self.contacts_map_form_class(
            request.POST,
            instance=self.object.map.last(),
        )
        seo_form = self.seo_form_class(
            request.POST,
            instance=self.object.seo,
        )
        if (
            contacts_page_form.is_valid() and
            contacts_address_form.is_valid() and
            contacts_map_form.is_valid() and
            seo_form.is_valid()
        ):
            return self.forms_valid(
                contacts_page_form,
                contacts_address_form,
                contacts_map_form,
                seo_form,
            )
        else:
            return self.forms_invalid(
                contacts_page_form,
                contacts_address_form,
                contacts_map_form,
                seo_form,
            )

    def forms_valid(
            self,
            contacts_page_form,
            contacts_address_form,
            contacts_map_form,
            seo_form,
    ):
        """
        Forms is valid
        """
        contacts_page_form.save()
        contacts_address_form.save()
        contacts_map_form.save()
        seo_form.save()
        return super(ContactsSettings, self).form_valid(seo_form)

    def forms_invalid(
            self,
            contacts_page_form,
            contacts_address_form,
            contacts_map_form,
            seo_form,
    ):
        """
        Forms is invalid
        """
        return self.render_to_response(
            self.get_context_data(
                contacts_page_form=contacts_page_form,
                contacts_address_form=contacts_address_form,
                contacts_map_form=contacts_map_form,
                seo_form=seo_form,
            )
        )
