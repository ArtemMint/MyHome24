from django import forms
from django.forms import inlineformset_factory

from admin_panel import models
from register import models as register_models


class HouseUserAdminForm(forms.ModelForm):
    prefix = 'house_user_admin'

    name = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control select-user',
            }
        ),
        queryset=register_models.User.users_admin.get_queryset(),
        label='ФИО',
    )

    class Meta:
        model = models.HouseUserAdmin
        fields = (
            'name',
            'role'
        )
        widgets = {
            'role': forms.TextInput(
                attrs={
                    'class': 'form-control user-role',
                    'readonly': 'True',
                }
            )
        }


HouseUserAdminFormset = inlineformset_factory(
    models.House,
    models.HouseUserAdmin,
    HouseUserAdminForm,
    extra=1,
    can_delete=True,
)
