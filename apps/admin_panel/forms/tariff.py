from django import forms

from admin_panel.models import (
    Tariff,
    TariffService,
)


class TariffForm(forms.ModelForm):
    prefix = 'tariff'

    class Meta:
        model = Tariff
        fields = (
            'name',
            'description',
            # 'editing_date',
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
            'editing_date': forms.DateTimeInput(
                format=('%Y-%m-%d'),
                attrs={'type': 'date'}),
        }


class TariffServiceForm(forms.ModelForm):
    prefix = 'tariff_service',

    class Meta:
        model = TariffService
        fields = (
            'service',
            'price',
            'currency',
            'metric',
        )
        widgets = {
            'service': forms.Select(
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
            'metric': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


TariffServiceDisplayFormset = forms.inlineformset_factory(
    Tariff,
    TariffService,
    TariffServiceForm,
    extra=0,
    can_delete=True,
)

TariffServiceFormset = forms.inlineformset_factory(
    Tariff,
    TariffService,
    TariffServiceForm,
    extra=1,
    can_delete=True,
)


