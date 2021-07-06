from django import forms
import django_filters
import datetime

from admin_panel import models


class CounterDataForm(forms.ModelForm):
    prefix = 'counter_data'

    house = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'house',
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
                'id': 'section',
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
                'id': 'flat',
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
                    '%m/%d/%Y'
                ),
                attrs={
                    # 'type': 'date',
                    'class': 'form-control',
                    'value': datetime.datetime.now().strftime("%m/%d/%Y"),
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


class CountersSearchForm(django_filters.FilterSet):

    house = django_filters.ModelChoiceFilter(
        queryset=models.House.get_houses_list(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'house',
                'onkeypress': 'form.submit();',
            }
        )
    )
    section = django_filters.ModelChoiceFilter(
        queryset=models.HouseSection.get_sections_list(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'section',
                'onkeypress': 'form.submit();',
            }
        )
    )
    flat = django_filters.ModelChoiceFilter(
        queryset=models.Flat.get_flats_list(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'flat',
                'onchange': 'form.submit();',
            }
        )
    )
    counter = django_filters.ModelChoiceFilter(
        queryset=models.Services.get_active_services(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'onchange': 'form.submit();',
            }
        )
    )
    number = django_filters.Filter(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'onchange': 'form.submit();',
            }
        )
    )
    # metric = django_filters.ModelChoiceFilter()

    class Meta:
        model = models.CounterData
        fields = (
            'house',
            'section',
            'flat',
            'counter',
            'value',
        )


class CounterListSearchForm(django_filters.FilterSet):
    STATUS = (
        ('Новое', 'Новое'),
        ('Учтено', 'Учтено'),
        ('Нулевое', 'Нулевое'),
    )
    number = django_filters.Filter(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'onchange': 'form.submit();',
            }
        )
    )
    status = django_filters.ChoiceFilter(
        choices=STATUS,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'onchange': 'form.submit();',
            }
        )
    )
    created_date = django_filters.DateFilter(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': ' form-control datepicker',
                'onchange': 'form.submit();',
            }
        )
    )
    house = django_filters.ModelChoiceFilter(
        queryset=models.House.get_houses_list(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'house',
                'onkeypress': 'form.submit();',
            }
        )
    )
    section = django_filters.ModelChoiceFilter(
        queryset=models.HouseSection.get_sections_list(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'section',
                'onkeypress': 'form.submit();',
            }
        )
    )
    flat = django_filters.ModelChoiceFilter(
        queryset=models.Flat.get_flats_list(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'flat',
                'onchange': 'form.submit();',
            }
        )
    )
    counter = django_filters.ModelChoiceFilter(
        queryset=models.Services.get_active_services(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'onchange': 'form.submit();',
            }
        )
    )
    # metric = django_filters.ModelChoiceFilter()

    class Meta:
        model = models.CounterData
        fields = (
            'number',
            'created_date',
            'status',
            'house',
            'section',
            'flat',
            'counter',
        )
