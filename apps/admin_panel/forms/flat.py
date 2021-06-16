from django import forms

from admin_panel import models
from register import models as reg_models


class FlatForm(forms.ModelForm):
    prefix = 'house_flat'
    owner = forms.ModelChoiceField(
        queryset=reg_models.User.users.get_queryset(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Владелец квартиры',
        required=False,
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
        }


class FlatCreateForm(FlatForm):
    account = forms.ModelChoiceField(
        queryset=models.Account.get_free_accounts(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Лицевой счет',
        required=False,
    )


class FlatUpdateForm(FlatForm):
    account = forms.ModelChoiceField(
        queryset=models.Account.get_accounts_list(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Лицевой счет',
        required=False,
    )
