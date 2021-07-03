from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from admin_panel import models, forms, utils, custom_views


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class CountersView(custom_views.ListFilteringView):
    model = models.CounterData
    search_form = forms.CountersSearchForm
    template_name = "admin_panel/counter_data/counters.html"


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class CounterListView(generic.View):
    model = models.CounterData
    search_class = forms.CounterListSearchForm
    template_name = 'admin_panel/counter_data/counters_list.html'

    def get(self, request, flat_pk):
        queryset = self.model.get_counter_data_list(
        ).filter(flat=flat_pk)
        f = self.search_class(
            request.GET,
            queryset=queryset,
        )
        return render(
            request,
            self.template_name,
            {
                'filter': f,
                'flat_pk': flat_pk,
            }
        )


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class CounterCreateView(generic.CreateView):
    model = models.CounterData
    form_class = forms.CounterDataForm
    template_name = 'admin_panel/counter_data/create.html'

    def get_initial(self):
        generated_number = utils.generate_number(self.model)
        date = utils.get_current_date()
        return {
            'number': generated_number,
            'created_date': date,
        }

    def get_success_url(self, **kwargs):
        return reverse("admin_panel:counter_detail", kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class CounterUpdateView(generic.UpdateView):
    model = models.CounterData
    form_class = forms.CounterDataForm
    template_name = 'admin_panel/counter_data/update.html'

    def get_success_url(self, **kwargs):
        return reverse("admin_panel:counter_detail", kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class CounterDetailView(generic.DetailView):
    model = models.CounterData
    context_object_name = 'counter_data'
    template_name = 'admin_panel/counter_data/detail.html'


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class CounterDeleteView(generic.View):
    model = models.CounterData
    success_url = 'admin_panel:counters'

    def get(self, request, pk):
        counter = self.model.get_counter_data_by_pk(pk)
        counter.delete()
        return redirect(self.success_url)
