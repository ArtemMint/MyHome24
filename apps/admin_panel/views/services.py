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
    # Formsets
    form_class = MetricsForm
    metrics_formset_class = MetricsFormset
    # Success URL
    success_url = reverse_lazy('admin_panel:service')
    # Success message
    success_message = 'Все данные успешно сохранены!'
    # Template to render
    template_name = "admin_panel/services/index.html"
    context_object_name = ('metrics_formset')

    # def __init__(self):
    #     super(ServicesAndMetricsList, self).__init__()
    #     self.object = self.get_object()

    def get_object(self, queryset=None):
        """
        Get object to render on page
        """
        obj, created = Metrics.objects.get_or_create(id=1)
        return obj


    def get_context_data(self, **kwargs):
        context = super(ServicesAndMetricsList, self).get_context_data()
        context['metrics_formset'] = Metrics.objects.all()
        return context
