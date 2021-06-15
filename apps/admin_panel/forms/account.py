from django import forms

from admin_panel import models


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
