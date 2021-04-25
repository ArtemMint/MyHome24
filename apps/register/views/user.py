from django.views.generic.base import TemplateView


class UserLoginPage(TemplateView):
    template_name = 'register/user/login.html'

class UserRegisterPage(TemplateView):
    template_name = 'register/user/register.html'
