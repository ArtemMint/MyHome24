from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages

from admin_panel import models
from admin_panel import forms


class HousesListView(generic.ListView):
    model = models.House
    context_object_name = 'houses_list'
    template_name = "admin_panel/houses/index.html"


def house_create_view(request):
    if request.POST:
        house_form = forms.HouseForm(
            request.POST or None,
            request.FILES,
        )
        house_preview_formset = forms.HousePreviewFormset(
            request.POST or None,
            request.FILES,
        )
        if house_form.is_valid() and house_preview_formset.is_valid():
            house_form.save()
            house_preview_formset.save()
            messages.success(request, 'Все обновлено!')
            return redirect('admin_panel:house_update')
    else:
        house_form = forms.HouseForm()
        house_preview_formset = forms.HousePreviewFormset()
    return render(
        request,
        'admin_panel/houses/create.html',
        {
            'house_form': house_form,
            'house_preview_formset': house_preview_formset,
        }
    )


def house_update_view(request, pk):
    if request.POST:
        house_form = forms.HouseForm(
            request.POST or None,
            request.FILES,
            instance=models.House.objects.get(id=pk),
        )
        house_preview_formset = forms.HousePreviewFormset(
            request.POST or None,
            request.FILES,
            instance=house_form.instance,
        )
        if house_form.is_valid() and \
                house_preview_formset.is_valid():
            house_form.save()
            house_preview_formset.save()
            messages.success(request, 'Все данные дома обновлены!')
            return redirect('admin_panel:house_update', pk)
    else:
        house_form = forms.HouseForm(
            instance=models.House.objects.get(id=pk),
        )
        house_preview_formset = forms.HousePreviewFormset(
            instance=house_form.instance,
        )
    return render(
        request,
        'admin_panel/houses/update.html',
        {
            'house_form': house_form,
            'house_preview_formset': house_preview_formset,
        }
    )


def house_detail_view(request, pk):
    try:
        house_preview = models.HousePreview.objects.filter(house=pk)
    except None:
        house_preview = False

    return render(
        request,
        'admin_panel/houses/detail.html',
        {
            'house_data': models.House.objects.get(id=pk),
            'house_preview': house_preview,
        }
    )


class HouseDeleteView(generic.DeleteView):
    model = models.House
    success_url = reverse_lazy('admin_panel:houses_list')
    template_name = 'admin_panel/houses/delete.html'
