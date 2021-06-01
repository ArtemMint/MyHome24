from django import forms
from datetime import datetime

from admin_panel import models
from register import models as register_models


class MasterRequestForm(forms.ModelForm):
    prefix = 'master_request'

    master = forms.ModelChoiceField(
        queryset=register_models.User.users_admin.get_queryset(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Мастер',
    )
    owner = forms.ModelChoiceField(
        queryset=register_models.User.users.get_queryset(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Владелец',
    )

    class Meta:
        model = models.MasterRequest
        fields = (
            'created_date',
            'time',
            'owner',
            'description',
            'flat',
            'master_type',
            'status',
            'master',
            'comment',
        )
        widgets = {
            'created_date': forms.DateInput(
                format=(
                    '%d-%m-%Y'
                ),
                attrs={
                    'type': 'date',
                    'class': 'form-control datepicker',
                    'value': datetime.now().strftime("%d/%m/%Y"),
                },
            ),
            'time': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control',
                },
            ),
            'owner': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Описание проблемы..',
                    'rows': 10,
                }
            ),
            'flat': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'master_type': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'status': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'master': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Описание проблемы..',
                    'rows': 5,
                }
            ),
        }
