from django.shortcuts import render
from django.views import generic

from register.models import User
from register.forms import


class UsersListView(generic.ListView):
    model = User
    context_object_name = 'users_list'
    template_name = "admin_panel/users/index.html"


def user_update_view(request, pk):
    if request.POST:



