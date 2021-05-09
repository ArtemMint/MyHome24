from django import forms
from django.forms import inlineformset_factory

from admin_panel import models


class HouseSectionForm(forms.ModelForm):
    class Meta:
        model = models.HouseSection
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


HouseSectionFormset = inlineformset_factory(
    models.House,
    models.HouseSection,
    HouseSectionForm,
    extra=1,
    can_delete=True,
)
