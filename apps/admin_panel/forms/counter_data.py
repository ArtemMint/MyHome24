from django import forms
import datetime

from admin_panel import models


class CounterDataForm(forms.ModelForm):
    prefix = 'counter_data'

    house = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        queryset=models.House.get_houses_list(),
        empty_label='Выберите...',
        label='Дом',
    )
    section = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        queryset=models.HouseSection.get_sections_list(),
        empty_label='Выберите...',
        label='Секция',
    )
    flat = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        queryset=models.Flat.get_flats_with_owner(),
        empty_label='Выберите...',
        label='Квартира',
    )
    counter = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        queryset=models.Services.get_active_services(),
        empty_label='Выберите...',
        label='Cчетчик',
    )

    class Meta:
        model = models.CounterData
        fields = (
            'number',
            'created_date',
            'value',
            'status',
            'house',
            'section',
            'flat',
            'counter',
        )

        widgets = {
            'number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Номер ведомости..',
                }
            ),
            'created_date': forms.DateInput(
                format=(
                    '%d-%m-%Y'
                ),
                attrs={
                    'class': 'form-control',
                },
            ),
            'status': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'value': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'number',
                    'placeholder': 'Введите показания..',
                }
            ),
        }
