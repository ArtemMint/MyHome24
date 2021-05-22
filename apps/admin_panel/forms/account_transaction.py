from django import forms

from admin_panel import models
from register import models as register_models


class AccountTransactionForm(forms.ModelForm):
    prefix = 'account_transaction'
    
    manager = forms.ModelChoiceField(
        queryset=register_models.User.get_users_admin_list(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    owner = forms.ModelChoiceField(
        queryset=register_models.User.get_active_users(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = models.AccountTransaction
        fields = (
            'number',
            'created_date',
            'confirm'
            'owner',
            'account',
            'transaction',
            'total',
            'manager',
            'comment',
        )

        widgets = {
            'number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'created_date': forms.DateInput(
                format=(
                    '%d-%m-%Y'
                ),
                attrs={
                    'type': "date",
                    'placeholder': 'Введите дату рождения',
                    'class': "form-control",
                }
            ),
            'confirm': forms.CheckboxInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'owner': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'total': forms.IntegerField(
                attrs={
                    'class': 'form-control',
                }
            ),
            'transaction': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'account': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Напишите комментарий..'
                }
            ),
        }
