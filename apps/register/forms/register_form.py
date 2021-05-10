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
            'full_name',
            'email',
            'password1',
            'password2',
        )

    # def clean(self):
    #     email = self.cleaned_data['email']
    #     name = self.cleaned_data['full_name'].split(' ')
    #     try:
    #         user = User.objects.get(email=email)
    #     except Exception as e:
    #         return None
    #     user.first_name = name[0]
    #     user.last_name = name[1]
    #     user.middle_name = name[2]
    #     user.save()

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            user = User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f'Email {email} уже успользуется.')
