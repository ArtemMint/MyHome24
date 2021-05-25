from django import forms

from admin_panel import models
from register import models as reg_models


class FlatForm(forms.ModelForm):
    prefix = 'house_flat'
    owner = forms.ModelChoiceField(
        queryset=reg_models.User.get_active_users(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Владелец квартиры',
    )

    class Meta:
        model = models.Flat
        fields = (
            'number',
            'area',
            'house',
            'section',
            'floor',
            'owner',
            'tariff',
            'account',
        )
        widgets = {
            'number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Номер квартиры..',
                }
            ),
            'area': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Площадь квартиры..',
                }
            ),
            'house': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'section': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'floor': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'tariff': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'account': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
