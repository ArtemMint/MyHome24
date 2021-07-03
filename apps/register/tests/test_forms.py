"""
Module with test forms
"""

from django.test import TestCase

from register import forms


class CreateUserFormTest(TestCase):
    def test_valid_label_form(self) -> None:
        form = forms.CreateUserForm()
        self.assertEqual(form.fields['first_name'].label, 'First name')
        self.assertEqual(form.fields['last_name'].label, 'Last name')
        self.assertEqual(form.fields['middle_name'].label, 'Middle name')

    def test_form_is_valid(self) -> None:
        form = forms.CreateUserForm(
            {
                'email': '123@gmail.com',
                'password1': 'admin',
                'password2': 'admin',
            },
        )
        self.assertTrue(form.is_valid(), 'Form isn`t valid.')

    def test_incorrect_email(self):
        form = forms.CreateUserForm(
            {
                'email': 'cooluser',
                'password1': 'admin',
                'password2': 'admin',
            },
        )
        self.assertFalse(form.is_valid())

    def test_uppercase_email(self):
        form = forms.CreateUserForm(
            {
                'email': 'USER@GMAIL.COM',
                'password1': 'admin',
                'password2': 'admin',
            },
        )
        self.assertTrue(form.is_valid())

    def test_birth_date_correct(self):
        form = forms.CreateUserForm(
            {
                'email': 'USER@GMAIL.COM',
                'password1': 'admin',
                'password2': 'admin',
                'birth_date': '1999-12-01'
            }
        )
        self.assertTrue(form.is_valid())

    def test_birth_date_incorrect_month(self):
        form1 = forms.CreateUserForm(
            {
                'email': 'USER@GMAIL.COM',
                'password1': 'admin',
                'password2': 'admin',
                'birth_date': '1999-13-01'
            }
        )
        form2 = forms.CreateUserForm(
            {
                'email': 'USER@GMAIL.COM',
                'password1': 'admin',
                'password2': 'admin',
                'birth_date': '1999.00.01'
            }
        )
        self.assertFalse(form1.is_valid())
        self.assertFalse(form2.is_valid())

    def test_birth_date_incorrect_day(self):
        form1 = forms.CreateUserForm(
            {
                'email': 'USER@GMAIL.COM',
                'password1': 'admin',
                'password2': 'admin',
                'birth_date': '1999-1-00'
            }
        )
        form2 = forms.CreateUserForm(
            {
                'email': 'USER@GMAIL.COM',
                'password1': 'admin',
                'password2': 'admin',
                'birth_date': '1999.1.32'
            }
        )
        self.assertFalse(form1.is_valid())
        self.assertFalse(form2.is_valid())


class UpdateUserFormTest(TestCase):
    def test_form_is_valid(self) -> None:
        form = forms.UpdateUserForm(
            {
                'email': 'user@gmail.com',
            },
        )
        self.assertTrue(form.is_valid(), 'Form isn`t valid.')
