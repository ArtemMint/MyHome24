from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from register import models
from register import forms

@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class UsersListView(generic.ListView):
    model = models.User
    context_object_name = 'users_list'
    template_name = "admin_panel/users/index.html"


@login_required(login_url='/admin/site/login')
def user_create_view(request):
    user_form = forms.UserCreateUserForm()
    if request.POST:
        user_form = forms.UserCreateUserForm(
            request.POST or None,
            request.FILES,
        )
        if user_form.is_valid():
            user = user_form.save(commit=False)
            raw_password = user_form.cleaned_data['password']
            user.set_password(raw_password)
            user.save()
            return redirect('admin_panel:users_list')
    return render(
        request,
        'admin_panel/users/create.html',
        {
            'user_form': user_form,
        }
    )


@login_required(login_url='/admin/site/login')
def user_update_view(request, pk):
    user_form = forms.UserCreateUserForm(
        instance=models.User.get_user_by_pk(pk),
        initial={
            'password': models.User.get_password(pk)
        }
    )
    if request.POST:
        user_form = forms.UserCreateUserForm(
            request.POST or None,
            request.FILES,
            instance=models.User.get_user_by_pk(pk),
        )
        if user_form.is_valid():
            user = user_form.save(commit=False)
            raw_password = user_form.cleaned_data['password']
            user.set_password(raw_password)
            user.save()
            return redirect('admin_panel:users_list')
    return render(
        request,
        'admin_panel/users/update.html',
        {
            'user_form': user_form,
        }
    )


@login_required(login_url='/admin/site/login')
def user_detail_view(request, pk):
    return render(
        request,
        'admin_panel/users/detail.html',
        {
            'user_form': models.User.get_user_by_pk(pk=pk)
        }
    )


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class UserDeleteView(generic.DeleteView):
    model = models.User
    success_url = reverse_lazy('admin_panel:users_list')
    template_name = 'admin_panel/users/delete.html'
