from django.shortcuts import render
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from admin_panel import models


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class FlatsList(generic.ListView):
    model = models.Flat
    template_name = "admin_panel/flats/index.html"


def flat_create_view(request):
    render(
        request,
        'admin_panel/flats/create.html',
        {

        }
    )


def flat_update_view(request):
    render(
        request,
        'admin_panel/flats/create.html',
        {

        }
    )


def flat_detail_view(request):
    render(
        request,
        'admin_panel/flats/create.html',
        {

        }
    )


class FlatDeleteView(generic.DeleteView):
    template_name = 'admin_panel/flats/delete.html'
