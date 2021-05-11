from django import forms
from django.forms import inlineformset_factory

from admin_panel import models


class FloorForm(forms.ModelForm):
    prefix = 'house_floor'

    class Meta:
        model = models.Floor
        fields = (
            'name',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


HouseFloorFormset = inlineformset_factory(
    models.House,
    models.HouseSection,
    FloorForm,
    extra=1,
    can_delete=True,
)
