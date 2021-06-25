import django_filters
from django import forms
from django.forms import inlineformset_factory

from admin_panel import models


class HouseForm(forms.ModelForm):
    prefix = 'house'

    class Meta:
        model = models.House
        fields = (
            'name',
            'address',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите название дома..',
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите адрес дома..',
                }
            ),
        }


class HousePreviewForm(forms.ModelForm):
    class Meta:
        model = models.HousePreview
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
    models.House,
    models.HousePreview,
    HousePreviewForm,
    extra=5,
    max_num=5,
)


class HouseFilter(django_filters.FilterSet):
    name = django_filters.Filter(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'onchange': 'form.submit();',
            }
        )
    )
    address = django_filters.Filter(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'onchange': 'form.submit();',
            }
        )
    )

    class Meta:
        model = models.House
        fields = (
            'name',
            'address',
        )
