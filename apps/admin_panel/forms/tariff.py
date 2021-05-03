from django import forms

from admin_panel.models import (
    Tariff,
    TariffService,
)


class TariffForm(forms.ModelForm):

    class Meta:
        model = Tariff
        fields = (
            'name',
            'description',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class TariffServiceForm(forms.ModelForm):

    class Meta:
        model = TariffService
        fields = (
            'service',
            'price',
            'currency',
            'metric',
        )
        widgets = {
            'service': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'currency': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'metric': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


TariffServiceFormset = forms.inlineformset_factory(
    Tariff,
    TariffService,
    TariffServiceForm,
    extra=1,
    can_delete=True,
)


