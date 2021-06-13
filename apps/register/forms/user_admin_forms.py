from django import forms

from register.models import User


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'phone',
            'role',
            'status',
            'email',
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
        }


class CreateUserAdminForm(UserAdminForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type': 'password',
            }
        ),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type': 'password',
            }
        ),
    )


class UpdateUserAdminForm(UserAdminForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type': 'password',
            }
        ),
        required=False,
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
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
