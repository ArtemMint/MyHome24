from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from register.models import User


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(
        max_length=255,
        help_text='Required. Add a valid email address.',
    )
    class Meta:
        model = User
        fields = (
            'email',
            'password1',
            'password2',
        )

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            user = User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f'Email {email} уже успользуется.')