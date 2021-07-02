from django.test import TestCase
from django.urls import reverse_lazy

from register import models


class UserLoginTest(TestCase):
    def setUp(self) -> None:
        self.user_data = {
            'email': 'user@gmail.com',
            'password': 'secret',
        }
        self.user = models.User.objects.create_user(**self.user_data)

    def tearDown(self) -> None:
        self.user.delete()

    def test_login_view(self):
        response = self.client.post(
            reverse_lazy('personal_cabinet:user_login'),
            self.user_data,
            follow=True,
        )
        self.assertTrue(response.context['user'].is_active)

    def test_login_view_wrong_password(self):
        user_data = {
            'email': 'user@gmail.com',
            'password': 'secret!23',
        }
        response = self.client.post(
            reverse_lazy('admin_panel:admin_login'),
            user_data,
            follow=True,
        )
        self.assertEqual(response.context['error_message'], 'Email or password not correct.')

    def test_login_view_wrong_email(self):
        user_data = {
            'email': 'us@gmail.com',
            'password': 'secret',
        }
        response = self.client.post(
            reverse_lazy('admin_panel:admin_login'),
            user_data,
            follow=True,
        )
        self.assertEqual(response.context['error_message'], 'Email or password not correct.')


class UserAdminLoginTest(TestCase):

    def setUp(self) -> None:
        self.user_data = {
            'email': 'admin@gmail.com',
            'password': 'secret',
        }
        self.user = models.User.objects.create_user(**self.user_data)

    def tearDown(self) -> None:
        self.user.delete()

    def test_login_and_logout_view(self):
        response = self.client.post(
            reverse_lazy('admin_panel:admin_login'),
            self.user_data,
            follow=True,
        )
        self.assertTrue(response.context['user'].is_active)
        response = self.client.post(
            reverse_lazy('admin_panel:admin_logout'),
            self.user_data,
            follow=True,
        )
        self.assertFalse(response.context['user'].is_active)

    def test_login_view_wrong_password(self):
        user_data = {
            'email': 'admin@gmail.com',
            'password': 'Secret1',
        }
        response = self.client.post(
            reverse_lazy('admin_panel:admin_login'),
            user_data,
            follow=True,
        )
        self.assertEqual(response.context['error_message'], 'Email or password not correct.')

    def test_login_view_wrong_email(self):
        user_data = {
            'email': 'admi@gmail.com',
            'password': 'secret',
        }
        response = self.client.post(
            reverse_lazy('admin_panel:admin_login'),
            user_data,
            follow=True,
        )
        self.assertEqual(response.context['error_message'], 'Email or password not correct.')
