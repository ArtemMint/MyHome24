"""
Services and metrics view
"""

from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from admin_panel.forms import (
    MetricsFormset,
    ServicesFormset,
)


def service_update_view(request):
    if request.POST:
        service_formset = ServicesFormset(
            request.POST,
        )
        if service_formset.is_valid():
            service_formset.save()
            return redirect('admin_panel:services_list')

    else:
        service_formset = ServicesFormset()
    return render(
        request,
        'admin_panel/services_metrics/services.html',
        {
            'service_formset': service_formset,
        }
    )


def metrics_update_view(request):
    if request.POST:
        metrics_formset = MetricsFormset(
            request.POST,
        )
        if metrics_formset.is_valid():
            metrics_formset.save()
            return redirect('admin_panel:metrics_list')

    else:
        metrics_formset = MetricsFormset()
    return render(
        request,
        'admin_panel/services_metrics/metrics.html',
        {
            'metrics_formset': metrics_formset,
        }
    )
