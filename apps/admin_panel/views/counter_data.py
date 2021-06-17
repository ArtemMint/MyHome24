from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from admin_panel import models
from admin_panel import forms


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class CountersView(generic.ListView):
    model = models.CounterData
    context_object_name = 'counter_data_list'
    template_name = "admin_panel/counter_data/counters.html"

    def get_queryset(self):
        return self.model.get_counter_data_list().order_by(
            'flat__number', 'counter__name'
        ).distinct('flat__number', 'counter__name')


class CountersListView(generic.View):
    model = models.CounterData
    template_name = 'admin_panel/counter_data/counters_list.html'

    def get(self, request, flat_pk):
        queryset = self.model.get_counter_data_list(
        ).filter(flat=flat_pk)
        return render(
            request,
            self.template_name,
            {
                'counters_by_flat': queryset,
            }
        )


class CounterCreateView(generic.CreateView):
    model = models.CounterData
    form_class = forms.CounterDataForm
    success_url = reverse_lazy('admin_panel:counters')
    template_name = 'admin_panel/counter_data/create.html'


class CounterUpdateView(generic.UpdateView):
    model = models.CounterData
    form_class = forms.CounterDataForm
    template_name = 'admin_panel/counter_data/update.html'

    def get_success_url(self, **kwargs):
        return reverse("admin_panel:counter_detail", kwargs={'pk': self.object.pk})


class CounterDetailView(generic.DetailView):
    model = models.CounterData
    context_object_name = 'counter_data'
    template_name = 'admin_panel/counter_data/detail.html'


class CounterDeleteView(generic.DeleteView):
    model = models.CounterData
    success_url = ''
