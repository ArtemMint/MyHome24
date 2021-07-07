import django_filters
from django import forms
from datetime import datetime

from admin_panel import models
from register import models as register_models


class MasterRequestForm(forms.ModelForm):
    prefix = 'master_request'

    master = forms.ModelChoiceField(
        queryset=register_models.User.users_admin.get_queryset(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Мастер',
        required=False,
    )
    owner = forms.ModelChoiceField(
        queryset=register_models.User.users.get_queryset(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Владелец',
        required=False,
    )

    class Meta:
        model = models.MasterRequest
        fields = (
            'created_date',
            'time',
            'owner',
            'description',
            'flat',
            'master_type',
            'status',
            'master',
            'comment',
        )
        widgets = {
            'created_date': forms.DateInput(
                format=(
                    '%d/%m/%Y'
                ),
                attrs={
                    # 'type': 'date',
                    'class': 'form-control datepicker',
                    'value': datetime.now().strftime("%d/%m/%Y"),
                },
            ),
            'time': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control',
                },
            ),
            'owner': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Описание проблемы..',
                    'rows': 10,
                }
            ),
            'flat': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'master_type': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'status': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'master': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Описание проблемы..',
                    'rows': 5,
                }
            ),
        }


class MasterRequestFilterForm(django_filters.FilterSet):
    STATUS = (
        ('Новое', 'Новое'),
        ('В работе', 'В работе'),
        ('Выполнено', 'Выполнено'),
    )
    MASTER_TYPE = (
        ('Любой специалист', 'Любой специалист'),
        ('Сантехник', 'Сантехник'),
        ('Слесарь', 'Слесарь'),
        ('Электрик', 'Электрик'),
    )

    id = django_filters.Filter(
        widget=forms.TextInput(
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
                'class': ' form-control daterangepicker',
                'onchange': 'form.submit();',
            }
        )
    )
    master_type = django_filters.ChoiceFilter(
        choices=MASTER_TYPE,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'onchange': 'form.submit();',
            }
        ),
    )
    description = django_filters.Filter(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
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
        queryset=register_models.User.get_active_users(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'onchange': 'form.submit();',
            }
        )
    )
    master = django_filters.ModelChoiceFilter(
        queryset=register_models.User.users_admin.get_queryset(),
        widget=forms.Select(
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

    class Meta:
        model = models.MasterRequest
        fields = (
            'id',
            'created_date',
            'owner',
            'description',
            'flat',
            'master_type',
            'status',
            'master',
        )