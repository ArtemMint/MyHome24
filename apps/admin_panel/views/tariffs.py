from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    DetailView,
)

from admin_panel.models import Tariff
from admin_panel.forms import (
    TariffForm,
    TariffServiceFormset,
    TariffServiceDisplayFormset,
)


class TariffList(ListView):
    queryset = Tariff.objects.all()
    template_name = "admin_panel/tariffs/index.html"


def tariff_update_view(request, pk):
    tariff_form = TariffForm(request.POST or None,
                             instance=Tariff.objects.get(id=pk))
    tariff_service_formset = TariffServiceDisplayFormset(
        request.POST or None,
        instance=Tariff.objects.get(id=pk),)
    if request.POST:
        if tariff_form.is_valid() and tariff_service_formset.is_valid():
            tariff_form.save()
            tariff_service_formset.save()
            return redirect('admin_panel:tariff_list')
    return render(
        request,
        'admin_panel/tariffs/create.html',
        {
            'tariff_form': tariff_form,
            'tariff_service_formset': tariff_service_formset,
        }
    )


def tariff_copy_view(request, pk):
    """
    Copy current item and save as new
    """
    tariff_form = TariffForm(
        request.POST or None,
        instance=Tariff.get_tariff_for_copy(pk=pk),)
    tariff_service_formset = TariffServiceDisplayFormset(
        request.POST or None,
        instance=Tariff.objects.get(id=pk),)

    if request.POST:
        if tariff_form.is_valid() \
                and tariff_service_formset.is_valid():
            tariff_form.save()
            tariff_service_formset.save()
            return redirect('admin_panel:tariff_list')

    return render(
        request,
        'admin_panel/tariffs/create.html',
        {
            'tariff_form': tariff_form,
            'tariff_service_formset': tariff_service_formset,
        }
    )


class TariffCreate(CreateView):
    model = Tariff
    form_class = TariffForm
    tariff_service_formset = TariffServiceFormset
    template_name = 'admin_panel/tariffs/create.html'
    success_url = reverse_lazy('admin_panel:tariff_list')

    def get_object(self, queryset=None):
        return Tariff.objects.create()

    def get_context_data(self, **kwargs):
        context = super(TariffCreate, self).get_context_data(**kwargs)
        context['tariff_form'] = self.form_class()
        context['tariff_service_formset'] = self.tariff_service_formset(
            instance=self.object,
        )
        return context

    def post(self, request, *args, **kwargs):
        tariff_form = self.form_class(
            request.POST,
        )
        tariff_service_formset = self.tariff_service_formset(
            request.POST,
            instance=tariff_form.instance,
        )
        if tariff_service_formset.is_valid() and tariff_form.is_valid():
            return self.forms_valid(tariff_form,
                                    tariff_service_formset,)
        else:
            return self.render_to_response(
                self.get_context_data(
                    tariff_form=self.form_class,
                    tariff_service_formset=self.tariff_service_formset,
                )
            )

    def forms_valid(self,
                    tariff_form,
                    tariff_service_formset,):
        tariff_form.save()
        for form in tariff_service_formset:
            form.save()
        return super(TariffCreate, self).form_valid(tariff_form)


class TariffDelete(DeleteView):
    model = Tariff
    template_name = 'admin_panel/tariffs/delete.html'
    success_url = reverse_lazy('admin_panel:tariff_list')


class TariffDetail(DetailView):
    template_name = 'admin_panel/tariffs/detail.html'
    success_url = reverse_lazy('admin_panel:tariff_list')
    context_object_name = 'tariff_form'
    tariff_service_formset = TariffServiceDisplayFormset

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return Tariff.objects.get(id=pk)

    def get_context_data(self, **kwargs):
        context = super(TariffDetail, self).get_context_data(**kwargs)
        context['tariff_service_formset'] = self.tariff_service_formset(
            instance=self.get_object(),
        )
        return context

    def get(self, request, *args, **kwargs):
        super(TariffDetail, self).get(request, *args, **kwargs)
        return self.render_to_response(
            self.get_context_data(
                object=self.object,  # instance is Tariff
                # All forms to render in page
                tariff_service_list=self.tariff_service_formset,
            )
        )
