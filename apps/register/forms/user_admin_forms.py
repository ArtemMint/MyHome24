from django import forms

from register.models import User


class UserAdminCreateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'phone',
            'role',
            'status'
            'email',
            'password1',
            'password2',
        )
        widgets = {
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
            'phone': forms.TextInput(
                attrs={
                    'input_type': 'text',
                    'class': 'form-control',
                }
            ),
            'role': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'status': forms.Select(
                attrs={
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
            # 'password1': forms.TextInput(
            #     attrs={
            #         # 'type': 'Password',
            #         'class': 'form-control',
            #     }
            # ),
            # 'password2': forms.TextInput(
            #     attrs={
            #         # 'type': 'Password',
            #         'class': 'form-control',
            #     }
            # ),
        }
