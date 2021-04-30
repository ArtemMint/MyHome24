"""
Services form
"""

from django import forms
from django.forms import modelformset_factory

from admin_panel.models import Services


class ServicesForm(forms.ModelForm):
    """
    Metrics form
    """

    class Meta:
        """
        Meta class
        """
        model = Services
        fields = (
            'name',
            'metric',
            'show_in_meter_reading',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'metric': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'show_in_meter_reading': forms.CheckboxInput(),
        }


ServicesFormset = modelformset_factory(
    Services,
    ServicesForm,
    fields=(
        'name',
        'metric',
        'show_in_meter_reading',
    ),
    extra=1,
)
