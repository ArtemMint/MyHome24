from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from admin_panel import models, forms, custom_views


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class FlatsListView(custom_views.ListFilteringView):
    model = models.Flat
    search_form = forms.FlatFilter
    template_name = 'admin_panel/flats/index.html'


@login_required(login_url='/admin/site/login')
def flat_create_view(request):
    flat_form = forms.FlatCreateForm()
    if request.POST:
        flat_form = forms.FlatCreateForm(
            request.POST,
        )
        if flat_form.is_valid():
            flat_form.save()
            messages.success(request, 'Новая квартира сохранена!')
            return redirect('admin_panel:flats_list')
    return render(
        request,
        'admin_panel/flats/create.html',
        {
            'flat_form': flat_form,
        }
    )


@login_required(login_url='/admin/site/login')
def flat_update_view(request, pk):
    flat_form = forms.FlatUpdateForm(
        instance=models.Flat.get_flat_by_pk(pk),
    )
    if request.POST:
        flat_form = forms.FlatUpdateForm(
            request.POST,
            instance=models.Flat.get_flat_by_pk(pk),
        )
        if flat_form.is_valid():
            flat_form.save()
            messages.success(request, 'Квартира обновлена!')
            return redirect('admin_panel:flats_list')
    return render(
        request,
        'admin_panel/flats/update.html',
        {
            'flat_form': flat_form,
        }
    )


@login_required(login_url='/admin/site/login')
def flat_detail_view(request, pk):
    return render(
        request,
        'admin_panel/flats/detail.html',
        {
            'flat_data': models.Flat.get_flat_by_pk(pk=pk),
        }
    )


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class FlatDeleteView(generic.DeleteView):
    model = models.Flat
    success_url = reverse_lazy('admin_panel:flats_list')
    template_name = 'admin_panel/flats/delete.html'
