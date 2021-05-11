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
    house_form = forms.HouseForm()
    house_preview_formset = forms.HousePreviewFormset()
    house_section_formset = forms.HouseSectionFormset()
    house_floor_formset = forms.HouseFloorFormset()
    if request.POST:
        house_form = forms.HouseForm(
            request.POST,
        )
        house_preview_formset = forms.HousePreviewFormset(
            request.POST,
            request.FILES,
        )
        house_section_formset = forms.HouseSectionFormset(
            request.POST,
            instance=house_form.instance,
        )
        house_floor_formset = forms.HouseFloorFormset(
            request.POST,
            instance=house_form.instance,
        )
        if house_form.is_valid() and\
                house_preview_formset.is_valid() and\
                house_section_formset.is_valid() and\
                house_floor_formset.is_valid():
            house_form.save()
            house_preview_formset.save()
            house_section_formset.save()
            house_floor_formset.save()
            messages.success(request, 'Все обновлено!')
            return redirect('admin_panel:houses_list')
        else:
            messages.error(request, 'Ошибка сохранения!')
    return render(
        request,
        'admin_panel/houses/create.html',
        {
            'house_form': house_form,
            'house_preview_formset': house_preview_formset,
            'house_section_formset': house_section_formset,
            'house_floor_formset': house_floor_formset,
        }
    )


def house_update_view(request, pk):
    house_form = forms.HouseForm(
        instance=models.House.objects.get(id=pk),
    )
    house_preview_formset = forms.HousePreviewFormset(
        instance=house_form.instance,
    )
    house_section_formset = forms.HouseSectionFormset(
        instance=house_form.instance,
    )
    house_floor_formset = forms.HouseFloorFormset(
        instance=house_form.instance,
    )
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
        house_section_formset = forms.HouseSectionFormset(
            request.POST,
            instance=house_form.instance,
        )
        house_floor_formset = forms.HouseFloorFormset(
            request.POST,
            instance=house_form.instance,
        )
        if house_form.is_valid() and \
                house_preview_formset.is_valid() and \
                house_section_formset.is_valid() and\
                house_floor_formset.is_valid():
            house_form.save()
            house_preview_formset.save()
            house_section_formset.save()
            house_floor_formset.save()
            messages.success(request, 'Все данные дома обновлены!')
            return redirect('admin_panel:houses_list')
    return render(
        request,
        'admin_panel/houses/update.html',
        {
            'house_form': house_form,
            'house_preview_formset': house_preview_formset,
            'house_section_formset': house_section_formset,
            'house_floor_formset': house_floor_formset,
        }
    )


def house_detail_view(request, pk):
    return render(
        request,
        'admin_panel/houses/detail.html',
        {
            'house_data': models.House.objects.get(id=pk),
            'house_preview': models.HousePreview.get_queryset_all_images(pk=pk),
            'house_section': models.HouseSection.get_sections_count(pk=pk),
            'house_floor': models.HouseFloor.get_sections_count(pk),
        }
    )


class HouseDeleteView(generic.DeleteView):
    model = models.House
    success_url = reverse_lazy('admin_panel:houses_list')
    template_name = 'admin_panel/houses/delete.html'
