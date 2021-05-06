from django import forms

from admin_panel.models.transaction_purpose import TransactionPurpose


class TransactionPurposeForm(forms.ModelForm):
    prefix = 'transaction_purpose'

    class Meta:
        model = TransactionPurpose
        fields = (
            'name',
            'type',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'type': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            )
        }
