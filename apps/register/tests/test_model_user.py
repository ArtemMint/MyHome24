"""
Module with test models
"""

from django.test import TestCase
from django.urls import reverse_lazy

from register import models


class UserAdminTest(TestCase):

    def setUp(self) -> None:
        self.admin = models.User.objects.create_superuser(
            email='admin@gmail.com',
            password='admin',
        )

    def test_create_admin(self):
        admin = self.admin
        self.assertEqual(admin.email, 'admin@gmail.com', 'Admin isn\'t created.')

    def test_is_admin(self):
        admin = self.admin
        self.assertTrue(admin.is_admin, 'Created user isn\'t admin.')

    def test_is_staff(self):
        admin = self.admin
        self.assertTrue(admin.is_staff, 'Created user isn\'t admin.')

    def test_is_superuser(self):
        admin = self.admin
        self.assertTrue(admin.is_superuser, 'Created user isn\'t admin.')

    def tearDown(self) -> None:
        self.admin.delete()


class UserTest(TestCase):

    def setUp(self) -> None:
        self.user_data = {
            'email': 'user@gmail.com',
            'password': 'secret',
        }
        self.user = models.User.objects.create_user(**self.user_data)

    def test_create_user(self):
        user = self.user
        self.assertEqual(user.email, 'user@gmail.com')

    def test_is_admin(self):
        user = self.user
        self.assertFalse(user.is_admin, 'Created user is admin.')

    def test_is_staff(self):
        user = self.user
        self.assertFalse(user.is_staff, 'Created user is admin.')

    def test_is_superuser(self):
        user = self.user
        self.assertFalse(user.is_superuser, 'Created user is admin.')

    def tearDown(self) -> None:
        self.user.delete()


class UserLoginTest(TestCase):
    def setUp(self) -> None:
        self.user_data = {
            'email': 'user@gmail.com',
            'password': 'secret',
        }
        self.user = models.User.objects.create_user(**self.user_data)

    def test_login(self):
        response = self.client.post(
            reverse_lazy('personal_cabinet:user_login'),
            self.user_data,
            follow=True,
        )
        self.assertTrue(response.context['user'].is_active)

    def tearDown(self) -> None:
        self.user.delete()
