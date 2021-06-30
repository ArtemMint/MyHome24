from django import forms
import django_filters

from admin_panel import models
from register import models as register_models


class FlatForm(forms.ModelForm):
    prefix = 'house_flat'
    owner = forms.ModelChoiceField(
        queryset=register_models.User.users.get_queryset(),
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
                    'id': 'house',
                }
            ),
            'section': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'section',
                }
            ),
            'floor': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'floor',
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


class FlatFilter(django_filters.FilterSet):
    number = django_filters.Filter(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'onchange': 'form.submit();',
            }
        )
    )
    house = django_filters.ModelChoiceFilter(
        queryset=models.House.get_houses_list(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'house',
                'onkeypress': 'form.submit();',
            }
        )
    )
    section = django_filters.ModelChoiceFilter(
        queryset=models.HouseSection.get_sections_list(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'section',
                'onkeypress': 'form.submit();',
            }
        )
    )
    floor = django_filters.ModelChoiceFilter(
        queryset=models.HouseFloor.get_floor_list(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'floor',
                'onchange': 'form.submit();',
            }
        )
    )
    owner = django_filters.ModelChoiceFilter(
        queryset=register_models.User.get_active_users(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'onchange': 'form.submit();',
            }
        )
    )

    class Meta:
        model = models.Flat
        fields = (
            'number',
            'house',
            'section',
            'floor',
            'owner',
        )
