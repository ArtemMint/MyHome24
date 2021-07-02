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

    def test_login(self):
        response = self.client.post(
            reverse_lazy('personal_cabinet:user_login'),
            self.user_data,
            follow=True,
        )
        self.assertTrue(response.context['user'].is_active)


class UserAdminLoginTest(TestCase):
    def setUp(self) -> None:
        self.user_data = {
            'email': 'admin@gmail.com',
            'password': 'secret',
        }
        self.user = models.User.objects.create_user(**self.user_data)

    def tearDown(self) -> None:
        self.user.delete()

    def test_login(self):
        response = self.client.post(
            reverse_lazy('admin_panel:admin_login'),
            self.user_data,
            follow=True,
        )
        self.assertTrue(response.context['user'].is_active)
