from django import forms

from register.models import User


class UserCreateForm(forms.ModelForm):

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
            'password',
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
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'middle_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
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
                    'placeholder': 'Введите описание',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'input_type': 'text',
                    'class': 'form-control',
                }
            ),
            'telegram': forms.TextInput(
                attrs={
                    'input_type': 'text',
                    'class': 'form-control',
                }
            ),
            'viber': forms.TextInput(
                attrs={
                    'input_type': 'text',
                    'class': 'form-control',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'type': 'email',
                    'class': 'form-control',
                }
            ),
            'password': forms.TextInput(
                attrs={
                    # 'type': 'Password',
                    'class': 'form-control',
                }
            ),
        }
