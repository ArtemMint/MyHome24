from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from register import models
from register import forms


@login_required(login_url='/admin/site/login')
def users_list_view(request):
    return render(
        request,
        "admin_panel/users/index.html",
        {
            'users_list': models.User.get_users_list(),
            'users_count': models.User.get_users_count(),
        }
    )


@login_required(login_url='/admin/site/login')
def user_create_view(request):
    user_form = forms.CreateUserForm()
    if request.POST:
        user_form = forms.CreateUserForm(
            request.POST or None,
            request.FILES,
        )
        if user_form.is_valid():
            user = user_form.save(commit=False)
            raw_password1 = user_form.cleaned_data['password1']
            raw_password2 = user_form.cleaned_data['password2']
            if raw_password1 == raw_password2:
                user.set_password(raw_password1)
                user.is_staff = True
                user.save()
                messages.success(request, 'Владелец квартиры создан!')
                return redirect('admin_panel:users_list')
            else:
                messages.success(request, 'Пароли не совпадают!')
        else:
            messages.success(request, 'Ошибка создания пользователя!')
    return render(
        request,
        'admin_panel/users/create.html',
        {
            'user_form': user_form,
        }
    )


@login_required(login_url='/admin/site/login')
def user_update_view(request, pk):
    user_form = forms.UpdateUserForm(
        instance=models.User.get_user_by_pk(pk),
    )
    if request.POST:
        user_form = forms.UpdateUserForm(
            request.POST or None,
            request.FILES,
            instance=models.User.get_user_by_pk(pk),
        )
        if user_form.is_valid():
            user = user_form.save(commit=False)
            raw_password1 = user_form.cleaned_data['password1']
            raw_password2 = user_form.cleaned_data['password2']
            if raw_password1 == raw_password2:
                user.set_password(raw_password1)
                user.is_staff = True
                user.save()
                messages.success(request, 'Владелец квартиры создан!')
                return redirect('admin_panel:users_list')
            else:
                messages.success(request, 'Пароли не совпадают!')
        else:
            messages.success(request, 'Ошибка создания пользователя!')
    return render(
        request,
        'admin_panel/users/update.html',
        {
            'user_form': user_form,
        }
    )


@login_required(login_url='/admin/site/login')
def user_detail_view(request, pk):
    user = models.User.get_user_by_pk(pk=pk)
    return render(
        request,
        'admin_panel/users/detail.html',
        {
            'user_form': user,
        }
    )


@method_decorator(login_required(login_url='/admin/site/login'), name='dispatch')
class UserDeleteView(generic.DeleteView):
    model = models.User
    success_url = reverse_lazy('admin_panel:users_list')
    template_name = 'admin_panel/users/delete.html'
