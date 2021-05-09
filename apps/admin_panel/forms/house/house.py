from django import forms
from django.forms import inlineformset_factory

from admin_panel.models import (
    House,
    HousePreview,
)

class HouseForm(forms.ModelForm):

    class Meta:
        model = House
        fields = (
            'name',
            'address',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


class HousePreviewForm(forms.ModelForm):
    class Meta:
        model = HousePreview
        fields = (
            'image',
        )
        widgets = {
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


HousePreviewFormset = inlineformset_factory(
    House,
    HousePreview,
    HousePreviewForm,
    extra=5,
    max_num=5,
    min_num=5,
)
