"""
Contacts forms for website
"""

from django import forms

from ...models import (
    ContactsPage,
    ContactsAddress,
    ContactsMap,
)


class ContactsPageForm(forms.ModelForm):
    """
    Contacts page form
    """

    class Meta:
        """
        Class Meta
        """
        model = ContactsPage
        fields = (
            'title',
            'short_text',
            'url',
        )
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'short_text': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '9'
                }
            ),
            'url': forms.URLInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class ContactsAddressForm(forms.ModelForm):
    """
    Contacts form with address
    """

    class Meta:
        """
        Class Meta
        """
        model = ContactsAddress
        fields = (
            'name',
            'location',
            'address',
            'phone',
            'email',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'location': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email':  forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class ContactsMapForm(forms.ModelForm):
    """
    Contacts form for map
    """

    class Meta:
        """
        Class Meta
        """
        model = ContactsMap
        fields = (
            'map',
        )
        widgets = {
            'map': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            )
        }
