"""
Services and metrics view
"""

from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from admin_panel.models import Services
from admin_panel.models import Metrics
from admin_panel.forms import ServicesFormset
from admin_panel.forms import MetricsFormset
from admin_panel.forms.services.metrics import MetricsForm


class ServicesAndMetricsList(SuccessMessageMixin, UpdateView):
    """ServicesAndMetricsList page is render page with forms and
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
    services_formset_class = ServicesFormset
    # Success URL
    success_url = reverse_lazy('admin_panel:service')
    # Success message
    success_message = 'Все данные успешно сохранены!'
    # Template to render
    template_name = "admin_panel/services/index.html"
    context_object_name = ('metrics_form')

    def __init__(self):
        super(ServicesAndMetricsList, self).__init__()
        self.object = self.get_object()

    def get_object(self, queryset=None):
        """
        Get object to render on page
        """
        obj, created = Services.objects.get_or_create(id=1)
        return obj


    def get_context_data(self, **kwargs):
        context = super(ServicesAndMetricsList, self).get_context_data()
        context['metrics_formset'] = self.metrics_formset_class(
        )
        context['services_formset'] = self.services_formset_class(
        )
        return context

    def get(self, request, *args, **kwargs):
        """
        GET method logic to render template page and all forms on it
        """
        super(ServicesAndMetricsList, self).get(request, *args, **kwargs)
        return self.render_to_response(
            self.get_context_data(
                object=self.object,
                metrics_formset=self.metrics_formset_class,
                services_formset=self.services_formset_class,
            )
        )

    def post(self, request, *args, **kwargs):
        """
        POST method logic to upade data in models
        using forms and instance as IndexPage
        """
        metrics_formset = self.metrics_formset_class(
            request.POST,
        )
        services_formset = self.services_formset_class(
            request.POST,
        )
        if metrics_formset.is_valid() and services_formset.is_valid():
            return self.forms_valid(
                metrics_formset,
                services_formset,
            )
        else:
            return self.forms_invalid(
                metrics_formset,
                services_formset,
            )

    def forms_valid(self,
                   metrics_formset,
                   services_formset):
        """
        Forms is valid save data in
        DB and call success message
        """

        metrics_formset.save()
        services_formset.save()
        return super(ServicesAndMetricsList, self).forms_valid(metrics_formset)

    def forms_invalid(self,
                      metrics_formset,
                      services_formset):
        """
        Forms is invalid.
        Render page without saving
        data and return errors
        """
        return self.render_to_response(
            self.get_context_data(
                metrics_formset=metrics_formset,
                services_formset=services_formset,
            )
        )

