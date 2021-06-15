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
        queryset=models.Flat.get_flats_list(),
        empty_label='Выберите...',
        label='Квартира',
    )
    counter = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        queryset=models.Metrics.get_metrics_list(),
        empty_label='Выберите...',
        label='Cчетчик',
    )
    status = forms.ChoiceField(
        widget=forms.Select(

        ),
        empty_label='Выберите...',
        label='Статус',
    )

    class Meta:
        model = models.CounterData
        fields = (
            'number',
            'created_date',
            'value',
            # 'status',
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
                    'type': 'date',
                    'class': 'form-control datepicker',
                    'value': datetime.datetime.now().strftime("%d/%m/%Y"),
                },
            ),
            # 'status': forms.Select(
            #     attrs={
            #         'class': 'form-control',
            #     }
            # ),
            'value': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'number',
                    'placeholder': 'Введите показания..',
                }
            ),
        }
