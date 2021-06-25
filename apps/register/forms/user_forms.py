from django import forms
import django_filters

from register.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'image',
            'status',
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'birth_date',
            'notes',
            'phone',
            'telegram',
            'viber',
            'email',
        )
        widgets = {
            'image': forms.FileInput(),
            'status': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'id': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите имя..',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите фамилию..',
                }
            ),
            'middle_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите отчество..',
                }
            ),
            'birth_date': forms.DateInput(
                format=(
                    '%Y-%m-%d'
                ),
                attrs={
                    'type': "date",
                    'placeholder': 'Введите дату рождения',
                    'class': "form-control",
                }
            ),
            'notes': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '11',
                    'placeholder': 'Напишите о себе...',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'input_type': 'text',
                    'class': 'form-control',
                    'placeholder': 'Введите ваш телефон +380991234567..',
                }
            ),
            'telegram': forms.TextInput(
                attrs={
                    'input_type': 'text',
                    'class': 'form-control',
                    'placeholder': 'Введите Telegram..',
                }
            ),
            'viber': forms.TextInput(
                attrs={
                    'input_type': 'text',
                    'class': 'form-control',
                    'placeholder': 'Введите Viber..',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'type': 'email',
                    'class': 'form-control',
                    'placeholder': 'Введите ваш e-mail..',
                }
            ),
        }


class CreateUserForm(UserForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control to_valid',
                'type': 'password',
            }
        ),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control to_valid',
                'type': 'password',
            }
        ),
    )


class UpdateUserForm(UserForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control to_valid',
                'type': 'password',
            }
        ),
        required=False,
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control to_valid',
                'type': 'password',
            }
        ),
        required=False,
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password1']
        if password:
            user.set_password(password)
        else:
            old_pass = User.objects.get(pk=self.instance.pk).password
            user.password = old_pass
        if commit:
            user.save()
        return user


class UserFilterForm(django_filters.FilterSet):
    STATUS = [
        ('Активен', 'Активен'),
        ('Новый', 'Новый'),
        ('Отключен', 'Отключен'),
    ]

    id = django_filters.Filter(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'onchange': 'form.submit();',
            }
        )
    )
    full_name = django_filters.Filter(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'onchange': 'form.submit();',
            }
        )
    )
    phone = django_filters.Filter(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'onchange': 'form.submit();',
            }
        )
    )
    email = django_filters.Filter(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'onchange': 'form.submit();',
            }
        )
    )
    date_joined = django_filters.DateFilter(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': ' form-control datepicker',
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
        model = User
        fields = (
            'id',
            'full_name',
            'phone',
            'email',
            'date_joined',
            'status',
        )

