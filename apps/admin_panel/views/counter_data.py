from django.shortcuts import render
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from admin_panel import models


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class CountersView(generic.ListView):
    queryset = models.CounterData.get_counter_data_list()
    template_name = "admin_panel/counter_data/counters.html"


class CountersListView(generic.ListView):
    template_name = 'admin_panel/counter_data/counters_list.html'


class CounterCreateView(generic.CreateView):
    template_name = 'admin_panel/counter_data/create.html'


class CounterUpdateView(generic.UpdateView):
    template_name = 'admin_panel/counter_data/update.html'


class CounterDetailView(generic.DetailView):
    template_name = 'admin_panel/counter_data/detail.html'


class CounterDeleteView(generic.DeleteView):
    model = models.CounterData
    success_url = ''
