from django import forms
import django_filters
from django_filters import DateFilter, ModelChoiceFilter

from admin_panel import models
from register import models as register_models


class AccountForm(forms.ModelForm):
    prefix = 'account'

    flat = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        queryset=models.Flat.get_free_flats(),
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
                }
            ),
            'section': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


# class AccountFilter(django_filters.FilterSet):
#     owner = ModelChoiceFilter(
#         queryset=register_models.User.get_active_users()
#     )
#     created_date = DateFilter(
#         widget=forms.DateInput(
#             attrs={
#                 'type': 'date',
#                 'class': 'datepicker',
#             }
#         )
#     )
#
#     class Meta:
#         model = models.AccountTransaction
#         fields = (
#             'number',
#             'status',
#             'house',
#             'section',
#             'flat',
#             'created_date',
#         )
