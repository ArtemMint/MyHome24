from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView

from django.contrib.messages.views import SuccessMessageMixin


from register.forms import (
    UserRegisterForm,
    UserAuthenticationForm,
)


class UserLoginView(LoginView):
    template_name = 'register/user/login.html'
    redirect_authenticated_user = True

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        context = {}

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(self.request.GET.get('next', 'personal_cabinet:summary'))
            else:
                context['error_message'] = "user is not active"
        else:
            context['error_message'] = "email or password not correct"

        return render(request, self.template_name, context)


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return reverse_lazy('personal_cabinet:user_login')


class UserRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'register/user/register.html'
    success_url = reverse_lazy('personal_cabinet:user_login')
    form_class = UserRegisterForm
    success_message = 'Вы успешло зарегистрированы.'
    context_object_name = 'registration_form'
