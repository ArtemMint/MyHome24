from django.shortcuts import render
from django.views import generic

from register.models import User


class UsersList(generic.ListView):
    model = User
    context_object_name = 'users_list'
    template_name = "admin_panel/users/index.html"
