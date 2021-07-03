"""
Module with test models
"""

from django.test import TestCase

from register import models


class UserAdminTest(TestCase):
    def setUp(self) -> None:
        self.admin = models.User.objects.create_superuser(
            email='admin@gmail.com',
            password='admin',
        )

    def tearDown(self) -> None:
        self.admin.delete()

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


class UserTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        user_data = {
            'email': 'user@gmail.com',
            'password': 'secret',
        }
        user_data2 = {
            'email': '123',
            'password': 'secret',
        }
        models.User.objects.create_user(**user_data)
        models.User.objects.create_user(**user_data2)

    @classmethod
    def tearDownClass(cls) -> None:
        user1 = models.User.objects.get(pk=1)
        user2 = models.User.objects.get(pk=2)
        user1.delete()
        user2.delete()

    def test_user_created(self):
        user = models.User.objects.get(pk=1)
        self.assertTrue(isinstance(user, models.User))
        self.assertTrue(user.check_password('secret'))
        self.assertEqual(user.email, 'user@gmail.com')

    def test_is_admin(self):
        user = models.User.objects.get(pk=1)
        self.assertFalse(user.is_admin, 'Created user is admin.')

    def test_is_staff(self):
        user = models.User.objects.get(pk=1)
        self.assertFalse(user.is_staff, 'Created user is admin.')

    def test_is_superuser(self):
        user = models.User.objects.get(pk=1)
        self.assertFalse(user.is_superuser, 'Created user is admin.')

    def test_all_users_created(self):
        number = models.User.objects.all().count()
        self.assertEqual(number, 2)
