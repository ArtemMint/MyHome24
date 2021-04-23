"""
Form for services page on website
"""

from django import forms

from ...models import ServicesPage, ServicesSite


class ServicesSiteForm(forms.ModelForm):
    """
    Services page form for
    updating data on website
    """

    class Meta:
        """
        Class Meta
        """
        model = ServicesSite
        fields = (
            'image',
            'name',
            'description',
        )
        widgets = {
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                },
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                },
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                },
            ),
        }

ServicesSiteFormset = forms.inlineformset_factory(
    ServicesPage,
    ServicesSite,
    ServicesSiteForm,
    fields=(
        'image',
        'name',
        'description',
    ),
    extra=1,
)
