"""
Pay-company form
"""

from django import forms

from admin_panel.models import PayCompany


class PayCompanyForm(forms.ModelForm):
    """
    Pay-company form
    """

    class Meta:
        """
        Meta class
        """
        model = PayCompany
        fields = (
            'name',
            'info',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'info': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            )
        }
