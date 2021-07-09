from django import forms
from datetime import datetime

from admin_panel import models


class UserMasterRequestForm(forms.ModelForm):
    prefix = 'master_request'

    class Meta:
        model = models.MasterRequest
        fields = (
            'created_date',
            'time',
            # 'owner',
            'description',
            'flat',
            'master_type',
            'status',
        )
        widgets = {
            'created_date': forms.DateInput(
                format=(
                    '%d/%m/%Y'
                ),
                attrs={
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
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Описание проблемы..',
                    'rows': 10,
                }
            ),
            'master_type': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
