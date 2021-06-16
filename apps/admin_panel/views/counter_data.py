from django.shortcuts import render
from django.urls import reverse_lazy
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


class CountersListView(generic.ListView):
    template_name = 'admin_panel/counter_data/counters_list.html'


class CounterCreateView(generic.CreateView):
    model = models.CounterData
    form_class = forms.CounterDataForm
    success_url = reverse_lazy('admin_panel:counters')
    template_name = 'admin_panel/counter_data/create.html'


class CounterUpdateView(generic.UpdateView):
    model = models.CounterData
    success_url = reverse_lazy('admin_panel:counters')
    template_name = 'admin_panel/counter_data/update.html'


class CounterDetailView(generic.DetailView):
    model = models.CounterData
    context_object_name = 'counter_data'
    template_name = 'admin_panel/counter_data/detail.html'


class CounterDeleteView(generic.DeleteView):
    model = models.CounterData
    success_url = ''
