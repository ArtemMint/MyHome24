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


# ServicesFormset = forms.modelformset_factory(
#     Services,
#     ServicesForm,
#     fields=(
#         'image',
#         'name',
#         'description',
#     ),
#     extra=3,
#     max_num=4,
#     min_num=4,
#     can_delete=True,
# )

ServicesFormset = forms.inlineformset_factory(
    ServicesPage,
    Services,
    ServicesForm,
    fields=(
        'image',
        'name',
        'description',
    ),
    extra=3,
    max_num=4,
    min_num=4,
    can_delete=True,
)
