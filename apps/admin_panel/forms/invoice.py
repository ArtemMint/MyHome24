import django_filters
from django import forms
import datetime

from admin_panel import models
from register import models as register_models


class InvoiceForm(forms.ModelForm):
    prefix = 'invoice'
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
            'tariff': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'account': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'start_date': forms.DateInput(
                format=(
                    '%m/%d/%Y'
                ),
                attrs={
                    # 'type': 'date',
                    'class': 'form-control',
                    'value': datetime.datetime.now().strftime("%m/%d/%Y"),
                },
            ),
            'end_date': forms.DateInput(
                format=(
                    '%m/%d/%Y'
                ),
                attrs={
                    # 'type': 'date',
                    'class': 'form-control',
                    'value': datetime.datetime.now().strftime("%m/%d/%Y"),
                },
            ),
        }

    def save(self, commit=True):
        instance = super(InvoiceForm, self).save(commit=False)
        instance.owner = models.Flat.objects.get(
            number=self.cleaned_data['flat'],
            house=self.cleaned_data['house'],
        ).owner
        instance.save()
        return instance


class InvoiceFilterForm(django_filters.FilterSet):
    STATUS = [
        ('Оплачена', 'Оплачена'),
        ('Частично оплачена', 'Частично оплачена'),
        ('Неоплачена', 'Неоплачена'),
    ]
    CONFIRM = [
        ('1', 'Проведена'),
        ('0', 'Непроведена'),
    ]

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
        ),
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
    flat = django_filters.ModelChoiceFilter(
        queryset=models.Flat.get_flats_list(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'onchange': 'form.submit();',
            }
        )
    )
    owner = django_filters.ModelChoiceFilter(
        queryset=register_models.User.get_users_list(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'onchange': 'form.submit();',
            }
        ),
    )
    confirm = django_filters.ChoiceFilter(
        choices=CONFIRM,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'onchange': 'form.submit();',
            }
        ),
    )

    class Meta:
        model = models.Invoice
        fields = '__all__'
        exclude = ['editing_date']
