from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView


class UserLoginView(LoginView):
    template_name = 'register/user/login.html'
    redirect_authenticated_user = True

    def get(self, request):
        return render(
            request,
            self.template_name
        )

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(
            email=email,
            password=password
        )
        context = {}
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(
                    self.request.GET.get('next', 'personal_cabinet:summary'),
                )
            else:
                context['error_message'] = "user is not active"
        else:
            context['error_message'] = "Email or password not correct"

        return render(
            request,
            self.template_name,
            context,
        )
