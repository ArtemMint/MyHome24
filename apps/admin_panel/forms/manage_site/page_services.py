"""
Form for services page on website
"""

from django import forms

from ...models import ServicesPage, Services


class ServicesForm(forms.ModelForm):
    """
    Services page form for
    updating data on website
    """

    class Meta:
        """
        Class Meta
        """
        model = Services
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

ServicesFormset = forms.inlineformset_factory(
    ServicesPage,
    Services,
    ServicesForm,
    fields=(
        'image',
        'name',
        'description',
    ),
    extra=1,
)
