from django import forms
from django.forms import inlineformset_factory

from admin_panel import models


class FloorForm(forms.ModelForm):
    prefix = 'house_floor'

    class Meta:
        model = models.HouseFloor
        fields = (
            'name',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Этаж..',
                }
            ),
        }


HouseFloorFormset = inlineformset_factory(
    models.House,
    models.HouseFloor,
    FloorForm,
    extra=1,
    can_delete=True,
)
