from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.views.generic import View
from django.contrib.auth.views import LoginView


class AdminLoginView(LoginView):
    template_name = 'register/admin/login.html'
    redirect_authenticated_user = True

    def get(self, request):
        return render(
            request,
            self.template_name,
        )

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email,
                            password=password,)
        context = {}

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(
                    self.request.GET.get('next', 'admin_panel:statistics')
                )
            else:
                context['error_message'] = "User is not active."
        else:
            context['error_message'] = "Email or password not correct."

        return render(
            request,
            self.template_name,
            context,
        )
