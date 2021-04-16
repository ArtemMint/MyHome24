"""
Views of site data
"""

# from django.contrib import messages
# from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView


from .. import models
from .. import forms


class IndexUpdate(SuccessMessageMixin, UpdateView):
    """
    Index page view class
    """
    model = models.IndexPage
    form_class = forms.IndexPageForm
    slider_formset_class = forms.IndexSliderFormset
    block_formset_class = forms.IndexBlockFormset
    seo_form_class = forms.SEOForm
    success_url = reverse_lazy('admin_panel:index')
    success_message = 'Все данные успешно сохранены!'
    template_name = 'admin_panel/manage_site/index.html'

    def __init__(self):
        super(IndexUpdate, self).__init__()
        self.object = self.get_object()

    def get_object(self, queryset=None):
        """
        Get index page data
        """
        obj = models.IndexPage.get_solo()
        if not obj.seo:
            obj.seo = models.SEO.objects.create().save()
        return obj

    def get_context_data(self, **kwargs):
        """
        Get context to render forms in page
        """
        context = super(IndexUpdate, self).get_context_data(**kwargs)
        context['index_form'] = self.form_class(
            instance=self.object,
        )
        context['slider_formset'] = self.slider_formset_class(
            instance=self.object,
        )
        context['block_formset'] = self.block_formset_class(
            instance=self.object,
        )
        context['seo_form'] = self.seo_form_class(
            instance=self.object.seo,
        )
        return context

    def get(self, request, *args, **kwargs):
        """
        GET method logic
        """
        super(IndexUpdate, self).get(request, *args, **kwargs)
        return self.render_to_response(
            self.get_context_data(
                object=self.object,
                index_form=self.form_class,
                slider_formset=self.slider_formset_class,
                block_formset=self.block_formset_class,
                seo_form=self.seo_form_class,
            )
        )

    def post(self, request, *args, **kwargs):
        """
        POST method logic
        """
        index_form = self.form_class(
            request.POST,
            instance=self.object,
        )
        slider_formset = self.slider_formset_class(
            request.POST,
            request.FILES,
            instance=self.object,
        )
        block_formset = self.block_formset_class(
            request.POST,
            request.FILES,
            instance=self.object,
        )
        seo_form = self.seo_form_class(
            request.POST,
            instance=self.object.seo,
        )
        if (
                index_form.is_valid() and
                slider_formset.is_valid() and
                block_formset.is_valid() and
                seo_form.is_valid()
        ):
            return self.forms_valid(
                index_form,
                slider_formset,
                block_formset,
                seo_form,
            )
        else:
            return self.forms_invalid(
                index_form,
                slider_formset,
                block_formset,
                seo_form,
            )

    def forms_valid(
            self,
            index_form,
            slider_formset,
            block_formset,
            seo_form,
    ):
        """
        Forms is valid
        """
        index_form.save()
        slider_formset.save()
        block_formset.save()
        seo_form.save()
        return super(IndexUpdate, self).form_valid(seo_form)

    def forms_invalid(
            self,
            index_form,
            slider_formset,
            block_formset,
            seo_form,
    ):
        """
        Forms is invalid
        """
        return self.render_to_response(
            self.get_context_data(
                index_form=index_form,
                slider_formset=slider_formset,
                block_formset=block_formset,
                seo_form=seo_form,
            )
        )


class AboutSettings(SuccessMessageMixin, UpdateView):
    models = models.AboutPage
    form_class = forms.AboutPageForm
    gallery_formset_class = forms.AboutGalleryFormset
    extra_info_formset_class = forms.AboutExtraInfoFormset
    extra_gallery_formset_class = forms.AboutExtraGalleryFormset
    extra_document_formset_class = forms.AboutDocumentFormset
    seo_form_class = forms.SEOForm
    success_url = reverse_lazy('admin_panel:about')
    success_message = 'Все данные успешно сохранены!'
    template_name = 'admin_panel/manage_site/about.html'

    def __init__(self):
        super(AboutSettings, self).__init__()
        self.object = self.get_object()
        self.documents = self.get_queryset()

    def get_object(self, queryset=None):
        """
        Get about page data
        """
        obj = models.AboutPage.get_solo()

        if not obj.seo:
            obj.seo = models.SEO.objects.create().save()
        return obj

    def get_queryset(self):
        """
        Get all documents
        """
        return models.AboutDocument.objects.all()

    def get_context_data(self, **kwargs):
        """
        Get context to render forms in page
        """
        context = super(AboutSettings, self).get_context_data(**kwargs)
        context['documents'] = self.documents
        context['about_page'] = models.AboutPage.get_solo()
        context['about_form'] = self.form_class(
            instance=self.object,
        )
        context['gallery_formset'] = self.gallery_formset_class(
            instance=self.object,
        )
        context['extra_info_formset'] = self.extra_info_formset_class(
            instance=self.object,
        )
        context['extra_gallery_formset'] = self.extra_gallery_formset_class(
            instance=self.object,
        )
        context['extra_document_formset'] = self.extra_document_formset_class(
            instance=self.object,
        )
        context['seo_form'] = self.seo_form_class(
            instance=self.object.seo,
        )
        return context

    def get(self, request, *args, **kwargs):
        """
        GET method logic
        """
        super(AboutSettings, self).get(request, *args, **kwargs)
        return self.render_to_response(
            self.get_context_data(
                object=self.object,
                about_form=self.form_class,
                gallery_formset=self.gallery_formset_class,
                extra_info_formset=self.extra_info_formset_class,
                extra_gallery_formset=self.extra_gallery_formset_class,
                documents=self.documents,
                seo_form=self.seo_form_class,
            )
        )

    def post(self, request, *args, **kwargs):
        """
        POST method logic
        """
        about_form = self.form_class(
            request.POST,
            request.FILES,
            instance=self.object,
        )
        gallery_formset = self.gallery_formset_class(
            request.POST,
            request.FILES,
            instance=self.object,
        )
        extra_info_formset = self.extra_info_formset_class(
            request.POST,
            instance=self.object,
        )
        extra_gallery_formset = self.extra_gallery_formset_class(
            request.POST,
            request.FILES,
            instance=self.object,
        )
        document_formset = self.extra_document_formset_class(
            request.POST,
            request.FILES,
            instance=self.object,
        )
        seo_form = forms.SEOForm(
            request.POST,
            instance=self.object.seo,
        )
        if (
                about_form.is_valid() and
                gallery_formset.is_valid() and
                extra_info_formset.is_valid() and
                extra_gallery_formset.is_valid() and
                document_formset.is_valid() and
                seo_form.is_valid()
        ):
            return self.forms_valid(
                about_form,
                gallery_formset,
                extra_info_formset,
                extra_gallery_formset,
                document_formset,
                seo_form
            )
        else:
            return self.forms_invalid(
                about_form,
                gallery_formset,
                extra_info_formset,
                extra_gallery_formset,
                document_formset,
                seo_form
            )

    def forms_valid(
            self,
            about_form,
            gallery_formset,
            extra_info_formset,
            extra_gallery_formset,
            document_formset,
            seo_form
    ):
        """
        Forms is invalid
        """
        about_form.save()
        gallery_formset.save()
        extra_info_formset.save()
        extra_gallery_formset.save()
        document_formset.save()
        seo_form.save()
        return super(AboutSettings, self).form_valid(seo_form)

    def forms_invalid(
            self,
            about_form,
            gallery_formset,
            extra_info_formset,
            extra_gallery_formset,
            document_formset,
            seo_form,
    ):
        """
        Forms is invalid
        """
        return self.render_to_response(
            self.get_context_data(
                about_form=about_form,
                gallery_formset=gallery_formset,
                extra_info_formset=extra_info_formset,
                extra_gallery_formset=extra_gallery_formset,
                document_formset=document_formset,
                seo_form=seo_form,
            )
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
    success_message = 'Все данные успешно сохранены!'
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
    success_message = 'Все данные успешно сохранены!'
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
