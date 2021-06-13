from django.db import models
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserAdminManager(models.Manager):
    """
    Class that filter only UserAdmin
    """
    def get_queryset(self):
        return super(UserAdminManager, self).get_queryset().filter(is_staff=True)


class OwnersManager(models.Manager):
    """
    Class that filter only UserAdmin
    """
    def get_queryset(self):
        return super(OwnersManager, self).get_queryset().filter(role='Владелец квартиры')
