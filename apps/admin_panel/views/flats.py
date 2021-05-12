from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from admin_panel import models
from admin_panel import forms


@login_required(login_url='/admin/site/login')
def flats_list_view(request):
    return render(
        request,
        'admin_panel/flats/index.html',
        {
            'flats_list': models.Flat.get_flats_list(),
            'flats_count': models.Flat.get_flats_count(),
        }
    )


def flat_create_view(request):
    flat_form = forms.FlatForm()
    if request.POST:
        flat_form = forms.FlatForm(
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


def flat_update_view(request, pk):
    flat_form = forms.FlatForm(
        instance=models.Flat.get_flat_by_pk(pk),
    )
    if request.POST:
        flat_form = forms.FlatForm(
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


def flat_detail_view(request, pk):
    return render(
        request,
        'admin_panel/flats/detail.html',
        {
            'flat_data': models.Flat.get_flat_by_pk(pk=pk),
        }
    )


class FlatDeleteView(generic.DeleteView):
    model = models.Flat
    success_url = reverse_lazy('admin_panel:flats_list')
    template_name = 'admin_panel/flats/delete.html'
