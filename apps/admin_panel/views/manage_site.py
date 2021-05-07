"""
Views of site data
"""


from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView

from admin_panel import models
from admin_panel import forms


class IndexSettings(SuccessMessageMixin, UpdateView):
    """IndexSettings page is render page with forms and
    data from DB and can change these data in forms

    Args:
        SuccessMessageMixin ([type]): success message 
        if all saved correct
        UpdateView ([type]): display all data
        using forms and update data in DB

    Returns:
        [type]: render page with all data
    """
    model = models.IndexPage
    # Forms
    form_class = forms.IndexPageForm
    slider_formset_class = forms.IndexSliderFormset
    block_formset_class = forms.IndexBlockFormset
    seo_form_class = forms.SEOForm
    # Success URL
    success_url = reverse_lazy('admin_panel:index')
    # Success message
    success_message = 'Все данные успешно сохранены!'
    # Template to render
    template_name = 'admin_panel/manage_site/index.html'

    def __init__(self):
        """
        Init start variable object - IndexPage
        """
        super(IndexSettings, self).__init__()  # init parent method
        self.object = self.get_object()  # get object IndexPage

    def get_object(self, queryset=None):
        """
        Get IndexPage data
        """
        # Get IndexPage instancesingletone
        obj: models.IndexPage = models.IndexPage.get_solo()
        if not obj.seo:
            # and create SEO connect if it`s empty
            obj.seo = models.SEO.objects.create().save()
        return obj

    def get_context_data(self, **kwargs):
        """
        Get context to rendering forms in page
        """
        context = super(IndexSettings, self).get_context_data(
            **kwargs)  # init parent method at first
        context['index_form'] = self.form_class(
            instance=self.object,  # instance is IndexPage
        )
        context['slider_formset'] = self.slider_formset_class(
            instance=self.object,  # instance is IndexPage
        )
        context['block_formset'] = self.block_formset_class(
            instance=self.object,  # instance is IndexPage
        )
        context['seo_form'] = self.seo_form_class(
            instance=self.object.seo,  # instance of SEO
        )
        return context

    def get(self, request, *args, **kwargs):
        """
        GET method logic to render template page and all forms on it
        """
        super(IndexSettings, self).get(request, *args,
                                       **kwargs)  # init parent method at first
        return self.render_to_response(
            self.get_context_data(
                object=self.object,  # IndexPage data
                # All forms
                index_form=self.form_class,
                slider_formset=self.slider_formset_class,
                block_formset=self.block_formset_class,
                seo_form=self.seo_form_class,
            )
        )

    def post(self, request, *args, **kwargs):
        """
        POST method logic to upade data in models
        using forms and instance as IndexPage
        """
        index_form = self.form_class(
            request.POST,
            instance=self.object,  # instance is IndexPage
        )
        slider_formset = self.slider_formset_class(
            request.POST,
            request.FILES,
            instance=self.object,  # instance is IndexPage
        )
        block_formset = self.block_formset_class(
            request.POST,
            request.FILES,
            instance=self.object,  # instance is IndexPage
        )
        seo_form = self.seo_form_class(
            request.POST,
            instance=self.object.seo,  # instance SEO
        )

        # verify if all forms is correct
        if (
                index_form.is_valid() and
                slider_formset.is_valid() and
                block_formset.is_valid() and
                seo_form.is_valid()
        ):
            # than return method forms_valid
            # that save all data in DB
            return self.forms_valid(
                index_form,
                slider_formset,
                block_formset,
                seo_form,
            )
        # else return method forms)invalid that
        # render page without saving data and
        # return errors
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
        Forms is valid save data in
        DB and call success message
        """
        index_form.save()
        slider_formset.save()
        block_formset.save()
        seo_form.save()
        return super(IndexSettings, self).form_valid(seo_form)

    def forms_invalid(
            self,
            index_form,
            slider_formset,
            block_formset,
            seo_form,
    ):
        """
        Forms is invalid.
        Render page without saving
        data and return errors
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
    """AboutSetting is render page with forms and
    data from DB and can change these data in forms

    Args:
        SuccessMessageMixin ([type]): success message 
        if all saved correct
        UpdateView ([type]): display all data
        using forms and update data in DB

    Returns:
        [type]: render page with all data
    """
    model = models.AboutPage
    # Forms
    form_class = forms.AboutPageForm
    gallery_formset_class = forms.AboutGalleryFormset
    extra_info_formset_class = forms.AboutExtraInfoFormset
    extra_gallery_formset_class = forms.AboutExtraGalleryFormset
    extra_document_formset_class = forms.AboutDocumentFormset
    seo_form_class = forms.SEOForm
    # Success URL
    success_url = reverse_lazy('admin_panel:about')
    # Success message
    success_message = 'Все данные успешно сохранены!'
    # Template ro render
    template_name = 'admin_panel/manage_site/about.html'

    def __init__(self):
        """
        Init start variable object - AboutPage
        documents - documents in About
        """
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
        Get context to rendering forms in page
        """
        context = super(AboutSettings, self).get_context_data(**kwargs)
        context['documents'] = self.documents
        context['about_page'] = models.AboutPage.get_solo()
        context['about_form'] = self.form_class(
            instance=self.object,  # instance is AboutPage
        )
        context['gallery_formset'] = self.gallery_formset_class(
            instance=self.object,  # instance is AboutPage
        )
        context['extra_info_formset'] = self.extra_info_formset_class(
            instance=self.object,  # instance is AboutPage
        )
        context['extra_gallery_formset'] = self.extra_gallery_formset_class(
            instance=self.object,  # instance is AboutPage
        )
        context['extra_document_formset'] = self.extra_document_formset_class(
            instance=self.object,  # instance is AboutPage
        )
        context['seo_form'] = self.seo_form_class(
            instance=self.object.seo,  # instance of SEO
        )
        return context

    def get(self, request, *args, **kwargs):
        """
        GET method logic to render template page and all forms on it
        """
        super(AboutSettings, self).get(request, *args, **kwargs)
        return self.render_to_response(
            self.get_context_data(
                object=self.object,   # instance is AboutPage
                # All forms to render in page
                about_form=self.form_class,
                gallery_formset=self.gallery_formset_class,
                extra_info_formset=self.extra_info_formset_class,
                extra_gallery_formset=self.extra_gallery_formset_class,
                seo_form=self.seo_form_class,
                # Documents
                documents=self.documents,
            )
        )

    def post(self, request, *args, **kwargs):
        """
        POST method logic to update data in models
        using forms and instance as IndexPage
        """
        about_form = self.form_class(
            request.POST,
            request.FILES,
            instance=self.object,  # instance is AboutPage
        )
        gallery_formset = self.gallery_formset_class(
            request.POST,
            request.FILES,
            instance=self.object,  # instance is AboutPage
        )
        extra_info_formset = self.extra_info_formset_class(
            request.POST,
            instance=self.object,  # instance is AboutPage
        )
        extra_gallery_formset = self.extra_gallery_formset_class(
            request.POST,
            request.FILES,
            instance=self.object,  # instance is AboutPage
        )
        document_formset = self.extra_document_formset_class(
            request.POST,
            request.FILES,
            instance=self.object,  # instance is AboutPage
        )
        seo_form = forms.SEOForm(
            request.POST,
            instance=self.object.seo,  # instance of SEO
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
        Forms is valid save data in
        DB and call success message
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
        Forms is invalid.
        Render page without saving
        data and return errors
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
    """ServicesSettings page is render page with forms and
    data from DB and can change these data in forms

    Args:
        SuccessMessageMixin ([type]): success message 
        if all saved correct
        UpdateView ([type]): display all data
        using forms and update data in DB

    Returns:
        [type]: render page with all data
    """
    model = models.ServicesPage
    # ALl forms
    form_class = forms.ServicesSiteForm
    formset_class = forms.ServicesSiteFormset
    second_form_class = forms.SEOForm
    # Success URL
    success_url = reverse_lazy('admin_panel:services_metrics')
    # Success message
    success_message = 'Все данные успешно сохранены!'
    # Template to render
    template_name = 'admin_panel/manage_site/services.html'

    def __init__(self):
        """
        Init start variable object - ServicePage
        """
        super(ServicesSettings, self).__init__()
        self.object = self.get_object()

    def get_object(self, queryset=None):
        """
        Get services_metrics page data
        """
        obj = models.ServicesPage.get_solo()
        if not obj.seo:
            obj.seo = models.SEO.objects.create()
            obj.save()
        return obj

    def get_context_data(self, **kwargs):
        """
        Get context to rendering forms in page
        """
        context = super(ServicesSettings, self).get_context_data(**kwargs)
        context['services_formset'] = self.formset_class(
            instance=self.object,  # instance is ServicesPage
        )
        context['seo_form'] = self.second_form_class(
            instance=self.object.seo,  # instance of SEO
        )
        return context

    def get(self, request, *args, **kwargs):
        """
        GET method logic to render template page and all forms on it
        """
        super(ServicesSettings, self).get(request, *args, **kwargs)
        return self.render_to_response(
            self.get_context_data(
                object=self.object,  # instance is ServicesPage
                # All forms
                services_formset=self.formset_class,
                seo_form=self.second_form_class,
            )
        )

    def post(self, request, *args, **kwargs):
        """
        POST method logic to upade data in models
        using forms and instance as IndexPage
        """
        formset = self.formset_class(
            request.POST,
            request.FILES,
            instance=self.object,  # instance is ServicesPage
        )
        form = self.second_form_class(
            request.POST,
            instance=self.object.seo,  # instance of SEO
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
        Forms is valid save data in
        DB and call success message
        """
        formset.save()
        form.save()
        return super(ServicesSettings, self).form_valid(form)

    def forms_invalid(self):
        """
        Forms is invalid.
        Render page without saving
        data and return errors
        """
        return self.render_to_response(
            self.get_context_data(
                services_formset=self.formset_class,
                seo_form=self.second_form_class,
            )
        )


class ContactsSettings(SuccessMessageMixin, UpdateView):
    """ContactsSettings page is render page with forms and
    data from DB and can change these data in forms

    Args:
        SuccessMessageMixin ([type]): success message 
        if all saved correct
        UpdateView ([type]): display all data
        using forms and update data in DB

    Returns:
        [type]: render page with all data
    """
    model = models.ContactsPage
    # Forms
    form_class = forms.ContactsPageForm
    contacts_address_form_class = forms.ContactsAddressForm
    contacts_map_form_class = forms.ContactsMapForm
    seo_form_class = forms.SEOForm
    # Success URL
    success_url = reverse_lazy('admin_panel:contacts')
    # Success message
    success_message = 'Все данные успешно сохранены!'
    # Template to render
    template_name = 'admin_panel/manage_site/contacts.html'

    def __init__(self):
        """
        Init start variable object - ContactsPage
        """
        super(ContactsSettings, self).__init__()
        self.object = self.get_object()

    def get_object(self, queryset=None):
        """
        Get contacts page data
        """
        obj = models.ContactsPage.get_solo()  # Get singleton
        if not obj.seo:
            # create seo connect
            obj.seo = models.SEO.objects.create()
        if obj.map.count() == 0:
            # create map connect
            obj.map.create()
        if obj.contacts_address.count() == 0:
            # Create address connect
            obj.contacts_address.create()
        obj.save()  # save changes
        return obj

    def get_context_data(self, **kwargs):
        """
        Get context to rendering forms in page
        """
        context = super(ContactsSettings, self).get_context_data(**kwargs)
        context['contacts_page_form'] = self.form_class(
            instance=self.object,  # instance is ContactsPage
        )
        context['contacts_address_form'] = self.contacts_address_form_class(
            instance=self.object.contacts_address.last(),  # instance is ContactsAddress
        )
        context['contacts_map_form'] = self.contacts_map_form_class(
            instance=self.object.map.last(),  # instance of ContactsMap
        )
        context['seo_form'] = self.seo_form_class(
            instance=self.object.seo,  # instance of SEO
        )
        return context

    def get(self, request, *args, **kwargs):
        """
        GET method logic to render template page and all forms on it
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
        POST method logic to upade data in models
        using forms and instance as IndexPage
        """
        contacts_page_form = self.form_class(
            request.POST,
            instance=self.object,  # instance is ContactsPage
        )
        contacts_address_form = self.contacts_address_form_class(
            request.POST,
            instance=self.object.contacts_address.last(),  # instance is ContactsAddress
        )
        contacts_map_form = self.contacts_map_form_class(
            request.POST,
            instance=self.object.map.last(),  # instance of ContactsMap
        )
        seo_form = self.seo_form_class(
            request.POST,
            instance=self.object.seo,  # instance of SEO
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
        Forms is valid save data in
        DB and call success message
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
        Forms is invalid.
        Render page without saving
        data and return errors
        """
        return self.render_to_response(
            self.get_context_data(
                contacts_page_form=contacts_page_form,
                contacts_address_form=contacts_address_form,
                contacts_map_form=contacts_map_form,
                seo_form=seo_form,
            )
        )
