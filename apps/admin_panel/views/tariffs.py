from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from admin_panel.models import (
    Tariff,
    TariffService,
)

from admin_panel.forms import (
    TariffForm,
    TariffServiceFormset,
)


class TariffList(ListView):
    queryset = Tariff.objects.all()
    template_name = "admin_panel/tariffs/index.html"


class TariffCreate(CreateView):
    queryset = Tariff.objects.all()
    form_class = TariffForm
    template_name = 'admin_panel/tariffs/create.html'
    success_url = reverse_lazy('admin_panel:tariff_list')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(TariffCreate, self).form_valid(form)


class TariffUpdate(UpdateView):
    queryset = Tariff.objects.all()
    form_class = TariffForm
    template_name = 'admin_panel/tariffs/create.html'
    success_url = reverse_lazy('admin_panel:tariff_list')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(TariffUpdate, self).form_valid(form)


class TariffDelete(DeleteView):
    model = Tariff
    template_name = 'admin_panel/tariffs/delete.html'
    success_url = reverse_lazy('admin_panel:tariff_list')


class TariffDetail(DetailView):
    queryset = Tariff.objects.all()
    template_name = 'admin_panel/tariffs/detail.html'
    success_url = reverse_lazy('admin_panel:tariff_list')
    context_object_name = 'tariff_form'
