from django import forms

from admin_panel import models


class FlatForm(forms.ModelForm):
    prefix = 'house_flat'

    class Meta:
        model = models.Flat
        fields = (
            'number',
            'area',
            'house',
            'section',
            'floor',
            'owner',
            'tariff',
        )
        house = forms.ModelChoiceField(
            queryset=models.House.objects.all()
        )
        section = forms.ModelChoiceField(
            queryset=models.HouseSection.objects.filter(house__name=house)
        )
        widgets = {
            'number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'area': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'house': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'section': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'floor': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'owner': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'tariff': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
