from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
)


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


def get_profile_image_filepath(self):
    return f'profile_images/{self.pk}/{"profile_image.png"}'


def get_default_profile_image():
    return 'default_profile_image.png'


class AbstractUser(AbstractBaseUser):
    """
    AbstractUser model is a base form other user model
    and contain register/login logic.
    """
    email = models.EmailField(
        verbose_name='email',
        max_length=100,
        unique=True,
    )
    date_joined = models.DateTimeField(
        verbose_name='date joined',
        auto_now_add=True,
    )
    last_login = models.DateTimeField(
        verbose_name='last login',
        auto_now=True,
    )
    is_admin = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    is_superuser = models.BooleanField(
        default=False,
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    class Meta:
        abstract = True

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class User(AbstractUser):
    """
    Custom User model to register and
    login users in application.
    """
    STATUS = (
        ('Активен', 'Активен'),
        ('Новый', 'Новый'),
        ('Отключен', 'Отключен')
    )
    ROLE = (
        ('Владелец квартиры', 'Владелец квартиры'),
        ('Директор', 'Директор'),
        ('Управляющий', 'Управляющий'),
        ('Бухгалтер', 'Бухгалтер'),
        ('Электрик', 'Электрик'),
        ('Сантехник', 'Сантехник'),
    )

    first_name = models.CharField(
        verbose_name='first name',
        max_length=50,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        verbose_name='last name',
        max_length=50,
        blank=True,
        null=True,
    )
    middle_name = models.CharField(
        verbose_name='middle name',
        max_length=50,
        blank=True,
        null=True,
    )
    phone = models.CharField(
        verbose_name='phone number',
        max_length=25,
        blank=True,
        null=False,
    )
    telegram = models.CharField(
        verbose_name='telegram',
        max_length=100,
        blank=True,
        null=True,
    )
    viber = models.CharField(
        verbose_name='viber',
        max_length=100,
        blank=True,
        null=True,
    )
    notes = models.TextField(
        verbose_name='notes about',
        max_length=1500,
        blank=True,
        null=True,
    )
    birth_date = models.DateField(
        verbose_name='date joined',
        auto_now_add=True,
        blank=True,
        null=True,
    )
    status = models.CharField(
        verbose_name='status of the user',
        max_length=100,
        blank=True,
        null=True,
        default=STATUS[1][0],
        choices=STATUS,
    )
    role = models.CharField(
        verbose_name='role of the user',
        max_length=150,
        blank=True,
        null=True,
        default=ROLE[0][0],
        choices=ROLE,
    )

    def get_full_name(self):
        return f'{self.first_name} {self.last_name} {self.middle_name}'


# class UserSocialNetwork(models.Model):
#     """
#     Social network of the user - Telegram and Viber
#     """
#     pass
#
#
# class UserProfile(models.Model):
#     """
#     Profile extend for User model
#     """
#     pass
#
#
# class UserPhone(models.Model):
#     """
#     Phone of the User
#     """
#     pass