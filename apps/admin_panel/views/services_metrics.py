"""
Services and metrics view
"""


from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from admin_panel import forms


@login_required(login_url='/admin/site/login')
def service_update_view(request):
    if request.POST:
        service_formset = forms.ServicesFormset(
            request.POST,
        )
        if service_formset.is_valid():
            service_formset.save()
            messages.success(request, 'Все услуги обновлены!')
            return redirect('admin_panel:services_list')
    else:
        service_formset = forms.ServicesFormset()
    return render(
        request,
        'admin_panel/services_metrics/services.html',
        {
            'service_formset': service_formset,
        }
    )


@login_required(login_url='/admin/site/login')
def metrics_update_view(request):
    if request.POST:
        metrics_formset = forms.MetricsFormset(
            request.POST,
        )
        if metrics_formset.is_valid():
            metrics_formset.save()
            messages.success(request, 'Все ед. изм. обновлены!')
            return redirect('admin_panel:metrics_list')

    else:
        metrics_formset = forms.MetricsFormset()
    return render(
        request,
        'admin_panel/services_metrics/metrics.html',
        {
            'metrics_formset': metrics_formset,
        }
    )
