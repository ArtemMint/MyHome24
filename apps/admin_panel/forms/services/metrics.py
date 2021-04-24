"""
Metrics form
"""

from django import forms
from django.forms import modelformset_factory

from admin_panel.models import Metrics


class MetricsForm(forms.ModelForm):
    """
    Metrics form
    """

    class Meta:
        """
        Meta class
        """
        model = Metrics
        fields = (
            'name',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


MetricsFormset = modelformset_factory(
    Metrics,
    MetricsForm,
    fields=('name',),
    extra=1,
)
