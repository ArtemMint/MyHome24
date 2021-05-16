from django import forms

from admin_panel import models


class AccountForm(forms.ModelForm):
    prefix = 'account'

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
            'flat': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
