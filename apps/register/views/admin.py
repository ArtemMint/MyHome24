from django.views.generic.base import TemplateView


class AdminLoginPage(TemplateView):
    template_name = 'register/admin/login.html'
