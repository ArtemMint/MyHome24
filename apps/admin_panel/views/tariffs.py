from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import generic

from admin_panel import models, forms


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class TariffList(generic.ListView):
    model = models.Tariff
    template_name = "admin_panel/tariffs/index.html"


@login_required(login_url='/admin/site/login')
def tariff_update_view(request, pk):
    tariff_form = forms.TariffForm(
        request.POST or None,
        instance=models.Tariff.objects.get(id=pk),
    )
    tariff_service_formset = forms.TariffServiceFormset(
        request.POST or None,
        instance=models.Tariff.objects.get(id=pk),
    )
    if request.POST:
        if tariff_form.is_valid() and \
                tariff_service_formset.is_valid():
            tariff_form.save()
            tariff_service_formset.save()
            messages.success(request, 'Все данные обновлены!')
            return redirect('admin_panel:tariff_update', pk)
    else:
        tariff_form = forms.TariffForm(
            instance=models.Tariff.objects.get(id=pk),
        )
        tariff_service_formset = forms.TariffServiceFormset(
            instance=models.Tariff.objects.get(id=pk),
        )

    return render(
        request,
        'admin_panel/tariffs/update.html',
        {
            'tariff_form': tariff_form,
            'tariff_service_formset': tariff_service_formset,
        }
    )


@login_required(login_url='/admin/site/login')
def tariff_copy_view(request, pk):
    """
    Copy current item and save as new
    """
    tariff_form = forms.TariffForm(
        request.POST or None,
        instance=models.Tariff.get_tariff_for_copy(pk=pk),
    )
    tariff_service_formset = forms.TariffServiceDisplayFormset(
        request.POST or None,
        instance=models.Tariff.objects.get(id=pk),
    )

    if request.POST:
        if tariff_form.is_valid() and \
                tariff_service_formset.is_valid():
            tariff_form.save()
            tariff_service_formset.save()
            messages.success(request, 'Создана новая копия!')
            return redirect('admin_panel:tariff_list')

    return render(
        request,
        'admin_panel/tariffs/update.html',
        {
            'tariff_form': tariff_form,
            'tariff_service_formset': tariff_service_formset,
        }
    )


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class TariffCreate(generic.CreateView):
    model = models.Tariff
    form_class = forms.TariffForm
    tariff_service_formset = forms.TariffServiceFormset
    template_name = 'admin_panel/tariffs/create.html'
    success_url = reverse_lazy('admin_panel:tariff_list')

    def get_object(self, queryset=None):
        return models.Tariff.objects.create()

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


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class TariffDelete(generic.DeleteView):
    model = models.Tariff
    template_name = 'admin_panel/tariffs/delete.html'
    success_url = reverse_lazy('admin_panel:tariff_list')


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class TariffDetail(generic.DetailView):
    template_name = 'admin_panel/tariffs/detail.html'
    success_url = reverse_lazy('admin_panel:tariff_list')
    context_object_name = 'tariff_form'
    tariff_service_formset = forms.TariffServiceDisplayFormset

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        obj = models.Tariff.objects.get(id=pk)
        return obj

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
                object=self.object,
                tariff_service_list=self.tariff_service_formset,
            )
        )
