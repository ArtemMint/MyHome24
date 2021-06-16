from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from admin_panel import models
from admin_panel import forms


@login_required(login_url='/admin/site/login')
def houses_list_view(request):
    return render(
        request,
        'admin_panel/houses/index.html',
        {
            'houses_list': models.House.get_houses_list(),
            'houses_count': models.House.get_houses_count(),
        }
    )


@login_required(login_url='/admin/site/login')
def house_create_view(request):
    house_form = forms.HouseForm()
    house_preview_formset = forms.HousePreviewFormset()
    house_section_formset = forms.HouseSectionFormset()
    house_floor_formset = forms.HouseFloorFormset()
    house_user_admin_formset = forms.HouseUserAdminFormset()
    if request.POST:
        house_form = forms.HouseForm(
            request.POST or None,
        )
        house_preview_formset = forms.HousePreviewFormset(
            request.POST or None,
            request.FILES,
            instance=house_form.instance,
        )
        house_section_formset = forms.HouseSectionFormset(
            request.POST or None,
            instance=house_form.instance,
        )
        house_floor_formset = forms.HouseFloorFormset(
            request.POST or None,
            instance=house_form.instance,
        )
        house_user_admin_formset = forms.HouseUserAdminFormset(
            request.POST or None,
            instance=house_form.instance,
        )
        if house_form.is_valid() and\
                house_preview_formset.is_valid() and\
                house_section_formset.is_valid() and\
                house_floor_formset.is_valid() and\
                house_user_admin_formset.is_valid():
            house_form.save()
            house_preview_formset.save()
            house_section_formset.save()
            house_floor_formset.save()
            house_user_admin_formset.save()
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
            'house_user_admin_formset': house_user_admin_formset,
        }
    )


@login_required(login_url='/admin/site/login')
def house_update_view(request, pk):
    house = models.House.get_house_by_pk(pk=pk)
    house_form = forms.HouseForm(
        instance=house,
    )
    house_preview_formset = forms.HousePreviewFormset(
        instance=house,
    )
    house_section_formset = forms.HouseSectionFormset(
        instance=house,
    )
    house_floor_formset = forms.HouseFloorFormset(
        instance=house,
    )
    house_user_admin_formset = forms.HouseUserAdminFormset(
        instance=house,
    )
    if request.POST:
        house_form = forms.HouseForm(
            request.POST or None,
            instance=models.House.get_house_by_pk(pk=pk),
        )
        house_preview_formset = forms.HousePreviewFormset(
            request.POST or None,
            request.FILES,
            instance=house_form.instance,
        )
        house_section_formset = forms.HouseSectionFormset(
            request.POST or None,
            instance=house_form.instance,
        )
        house_floor_formset = forms.HouseFloorFormset(
            request.POST or None,
            instance=house_form.instance,
        )
        house_user_admin_formset = forms.HouseUserAdminFormset(
            request.POST or None,
            instance=house_form.instance,
        )
        if house_form.is_valid() and\
                house_preview_formset.is_valid() and\
                house_section_formset.is_valid() and\
                house_floor_formset.is_valid() and \
                house_user_admin_formset.is_valid():
            house_form.save()
            house_preview_formset.save()
            house_section_formset.save()
            house_floor_formset.save()
            house_user_admin_formset.save()
            messages.success(request, 'Все данные дома обновлены!')
            return redirect('admin_panel:houses_list')
        else:
            messages.error(request, 'Ошибка сохранения!')
            return redirect('admin_panel:house_update', pk=pk)
    return render(
        request,
        'admin_panel/houses/update.html',
        {
            'house_form': house_form,
            'house_preview_formset': house_preview_formset,
            'house_section_formset': house_section_formset,
            'house_floor_formset': house_floor_formset,
            'house_user_admin_formset': house_user_admin_formset,
        }
    )


@login_required(login_url='/admin/site/login')
def house_detail_view(request, pk):
    return render(
        request,
        'admin_panel/houses/detail.html',
        {
            'house_data': models.House.objects.get(id=pk),
            'house_preview': models.HousePreview.get_queryset_all_images(pk=pk),
            'house_section': models.HouseSection.get_sections_count(pk=pk),
            'house_floor': models.HouseFloor.get_floor_count(pk),
            'house_user_admin_list': models.HouseUserAdmin.get_user_admin_list(pk=pk),
        }
    )


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class HouseDeleteView(generic.DeleteView):
    model = models.House
    success_url = reverse_lazy('admin_panel:houses_list')
    template_name = 'admin_panel/houses/delete.html'
