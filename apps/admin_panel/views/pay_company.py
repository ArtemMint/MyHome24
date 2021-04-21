"""
Pay company view
"""

from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from apps.admin_panel import models
from apps.admin_panel import forms


class PayCompany(SuccessMessageMixin, UpdateView):
    """PayCompany view that can update and
    display all information about pay company

    Args:
        SuccessMessageMixin ([type]): success message 
        if all saved correct
        UpdateView ([type]): display all data
        using forms and update data in DB
    """
    model = models.PayCompany
    form_class = forms.PayCompanyForm
    success_url = reverse_lazy('admin_panel:pay_company')
    success_message = 'Все данные успешно сохранены!'
    template_name = "admin_panel/pay_company/index.html"
    
    def get_object(self):
        """
        Get qobject to render on page
        """
        return models.PayCompany.objects.get(id=1)
