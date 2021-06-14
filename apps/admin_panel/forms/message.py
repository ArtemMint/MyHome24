from django import forms

from admin_panel import models


class MessageForm(forms.ModelForm):
    prefix = 'message'

    house = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        queryset=models.House.get_houses_list(),
        required=False,
        empty_label='Всем...',
        label='Дом',
    )
    section = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        queryset=models.HouseSection.get_sections_list(),
        required=False,
        empty_label='Всем...',
        label='Секция',
    )
    floor = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        queryset=models.HouseFloor.get_floor_list(),
        required=False,
        empty_label='Всем...',
        label='Этаж',
    )
    flat = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        queryset=models.Flat.get_flats_list(),
        required=False,
        empty_label='Всем...',
        label='Квартира',
    )

    class Meta:
        model = models.Message
        fields = (
            'title',
            'text',
            'indebtedness',
            'house',
            'section',
            'floor',
            'flat',
        )
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Тема сообщения:',
                }
            ),
            'text': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Текст сообщения:',
                }
            ),
            'indebtedness': forms.CheckboxInput(),
        }
