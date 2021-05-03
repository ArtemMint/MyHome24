from django.views.generic.list import ListView

from admin_panel.models import (
    Tariff,
    TariffService,
)

from admin_panel.forms import (
    TariffForm,
    TariffServiceFormset,
)


class TariffsList(ListView):
    model = Tariff
    form = TariffForm
    template_name = "admin_panel/tariffs/index.html"
    context_object_name = 'tariff_form'
