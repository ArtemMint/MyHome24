"""
Services and metrics view
"""

from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from admin_panel.models import Services
from admin_panel.models import Metrics
from admin_panel.forms import (
    MetricsForm,
    MetricsFormset,
    ServicesForm,
    ServicesFormset,
)


class MetricsList(SuccessMessageMixin, UpdateView):
    """MetricsList page is render page with forms and
    data from DB and can change these data in forms

    Args:
        SuccessMessageMixin ([type]): success message
        if all saved correct
        UpdateView ([type]): display all data
        using forms and update data in DB

    Returns:
        [type]: render page with all data
    """
    model = Metrics
    # Forms
    form_class = MetricsForm
    metrics_formset_class = MetricsFormset
    # Success URL
    success_url = reverse_lazy('admin_panel:metrics_list')
    # Success message
    success_message = 'Все данные успешно сохранены!'
    # Template to render
    template_name = "admin_panel/services_metrics/metrics.html"
    context_object_name = 'metrics_formset'

    def get_object(self, queryset=None):
        return Metrics.objects.first()

    def get(self, request, *args, **kwargs):
        """
        GET method logic to render template page and all forms on it
        """
        super(MetricsList, self).get(request, *args, **kwargs)
        return self.render_to_response(
            self.get_context_data(
                metrics_formset=self.metrics_formset_class,
            )
        )

    def post(self, request, *args, **kwargs):
        """
        POST method logic to update data in models
        using forms and instance as IndexPage
        """
        metrics_formset = self.metrics_formset_class(
            request.POST,
            queryset=Metrics.objects.all()
        )
        if metrics_formset.is_valid():
            return self.form_valid(
                metrics_formset,
            )
        else:
            return self.form_invalid(
                metrics_formset,
            )

    def form_valid(self,
                   metrics_formset,):
        """
        Forms is valid save data in
        DB and call success message
        """
        metrics_formset.save()
        for form in metrics_formset:
            form.save()
        return super(MetricsList, self).form_valid(form)

    def form_invalid(self,
                     metrics_formset,):
        """
        Forms is invalid.
        Render page without saving
        data and return errors
        """
        self.object = self.get_object()
        return self.render_to_response(
            self.get_context_data(
                metrics_formset=self.metrics_formset_class,
            )
        )

class ServicesList(SuccessMessageMixin, UpdateView):
    """ServicesList page is render page with forms and
    data from DB and can change these data in forms

    Args:
        SuccessMessageMixin ([type]): success message
        if all saved correct
        UpdateView ([type]): display all data
        using forms and update data in DB

    Returns:
        [type]: render page with all data
    """
    model = Services
    # Forms
    form_class = ServicesForm
    services_formset_class = ServicesFormset
    # Success URL
    success_url = reverse_lazy('admin_panel:services_list')
    # Success message
    success_message = 'Все данные успешно сохранены!'
    # Template to render
    template_name = "admin_panel/services_metrics/services.html"
    context_object_name = 'services_formset'

    def __init__(self):
        super(ServicesList, self).__init__()
        self.object = self.get_object()

    def get_object(self, queryset=None):
        return Services.objects.first()

    def get(self, request, *args, **kwargs):
        """
        GET method logic to render template page and all forms on it
        """
        super(ServicesList, self).get(request, *args, **kwargs)
        return self.render_to_response(
            self.get_context_data(
                services_formset=self.services_formset_class,
            )
        )

    def post(self, request, *args, **kwargs):
        """
        POST method logic to update data in models
        using forms and instance as IndexPage
        """
        services_formset = self.services_formset_class(
            request.POST,
        )
        if services_formset.is_valid():
            return self.form_valid(
                services_formset,
            )
        else:
            return self.form_invalid(
                services_formset,
            )

    def form_valid(self,
                   services_formset,):
        """
        Forms is valid save data in
        DB and call success message
        """
        services_formset.save()
        for form in services_formset:
            form.save()
        return super(ServicesList, self).form_valid(form)

    def form_invalid(self,
                     services_formset,):
        """
        Forms is invalid.
        Render page without saving
        data and return errors
        """
        return self.render_to_response(
            self.get_context_data(
                services_formset=self.services_formset_class,
            )
        )
