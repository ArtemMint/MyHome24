from django import forms
import datetime

from admin_panel import models


class InvoiceForm(forms.ModelForm):
    house = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        queryset=models.House.get_houses_list(),
        label='Дом',
    )
    section = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        queryset=models.HouseSection.get_sections_list(),
        label='Секция',
    )
    flat = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        queryset=models.Flat.get_flats_with_owner(),
        label='Квартира',
    )

    class Meta:
        model = models.Invoice
        fields = '__all__'
        exclude = ['editing_date']
        widgets = {
            'number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Заполните номер квитанции..',
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
            'status': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'tariff': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'start_date': forms.DateInput(
                format=(
                    '%d-%m-%Y'
                ),
                attrs={
                    'type': 'date',
                    'class': 'form-control datepicker',
                    'value': datetime.datetime.now().strftime("%d/%m/%Y"),
                },
            ),
            'end_date': forms.DateInput(
                format=(
                    '%d-%m-%Y'
                ),
                attrs={
                    'type': 'date',
                    'class': 'form-control datepicker',
                    'value': datetime.datetime.now().strftime("%d/%m/%Y"),
                },
            ),
        }
