from django import forms
import django_filters

from admin_panel import models
from register import models as register_models


class AccountForm(forms.ModelForm):
    prefix = 'account'

    flat = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'flat',
            }
        ),
        queryset=models.Flat.get_flats_list(),
        label='Квартира',
        required=False,
    )

    class Meta:
        model = models.Account
        fields = (
            'number',
            'status',
            'house',
            'section',
            'flat',
        )
        widgets = {
            'number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Заполните номер лицевого счета..',
                }
            ),
            'status': forms.Select(
                attrs={
                    'class': 'form-control',
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
        }


class AccountFilter(django_filters.FilterSet):
    STATUS = [
        ('Активен', 'Активен'),
        ('Неактивен', 'Неактивен')
    ]

    number = django_filters.Filter(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'onchange': 'form.submit();',
            }
        )
    )
    status = django_filters.ChoiceFilter(
        choices=STATUS,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'onchange': 'form.submit();',
            }
        )
    )
    flat = django_filters.ModelChoiceFilter(
        queryset=models.Flat.get_flats_list(),
        widget=forms.Select(
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
    # owner = django_filters.ModelChoiceFilter(
    #     queryset=register_models.User.get_active_users(),
    #     widget=forms.Select(
    #         attrs={
    #             'class': 'form-control',
    #             'onchange': 'form.submit();',
    #         }
    #     )
    # )

    class Meta:
        model = models.Account
        fields = (
            'number',
            'status',
            'house',
            'section',
            'flat',
        )
