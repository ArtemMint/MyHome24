from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from admin_panel import models, views


class MasterRequestListView(generic.ListView):
    model = models.MasterRequest
    context_object_name = 'master_request_list'
    template_name = "personal_cabinet/master_request/index.html"

    def get_queryset(self):
        user = self.request.user.id
        user_requests = self.model.objects.filter(owner=user)
        return user_requests


class MasterRequestDeleteView(generic.DeleteView):
    model = models.MasterRequest
    template_name = 'personal_cabinet/master_request/delete.html'

    def get_success_url(self):
        return reverse_lazy('personal_cabinet:master_request_list')
