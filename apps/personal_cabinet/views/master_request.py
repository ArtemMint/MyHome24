from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic

from admin_panel import models, views
from personal_cabinet import forms


class MasterRequestListView(generic.ListView):
    model = models.MasterRequest
    context_object_name = 'master_request_list'
    template_name = "personal_cabinet/master_request/index.html"

    def get_queryset(self):
        user = self.request.user.id
        user_requests = self.model.objects.filter(owner=user)
        return user_requests


class MasterRequestCreateView(generic.View):
    model = models.MasterRequest
    form_class = forms.UserMasterRequestForm
    template_name = 'personal_cabinet/master_request/create.html'

    def get(self, request):
        form = self.form_class()
        return self.render_template(form)

    def post(self, request):
        user = request.user
        form = self.form_class(
            request.POST,
        )
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = user
            obj.save()
            return redirect('personal_cabinet:master_request_list')
        else:
            return self.render_template(form)

    def render_template(self, form):
        return render(
            self.request,
            self.template_name,
            {
                'form': form,
            }
        )


class MasterRequestDeleteView(generic.DeleteView):
    model = models.MasterRequest
    template_name = 'personal_cabinet/master_request/delete.html'

    def get_success_url(self):
        return reverse_lazy('personal_cabinet:master_request_list')
