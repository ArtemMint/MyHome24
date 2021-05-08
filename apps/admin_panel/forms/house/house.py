from django import forms
from django.forms import modelformset_factory

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


class HousePreviewForm(forms.ModelForm):
    class Meta:
        model = HousePreview
        fields = (
            'image',
        )


HousePreviewFormset = modelformset_factory(
    HousePreview,
    HousePreviewForm,
    extra=0,
)
